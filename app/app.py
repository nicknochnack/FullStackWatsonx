"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
from app.client import codegen, landing, clientdiscovery


from app.config.state import State
from app.config import style
from app.components.chat import chat_live_client, chat_live_bot, action_bar_livechat
from app.components.layout import info_box
from app.components.navbar import navbar

# Import Langchain interface  and use base chain
from app.utils.watsonxga import WatsonxLangchainLLM
from app.utils.vectorstore import VectorStore
from app.utils.prompts import ragprompt

from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

import os

os.environ["TOKENIZERS_PARALLELISM"] = "False"

llm = WatsonxLangchainLLM(
    model_id=ModelTypes.LLAMA_2_70B_CHAT.value,
    generate_params={
        GenParams.DECODING_METHOD: "greedy",
        GenParams.MAX_NEW_TOKENS: 200,
    },
).from_pretrained()

store = VectorStore("assets/ibmfaqs.pdf")


# Keep track of tokens associated with the same client browser ("shared" sessions)
shared_sessions_by_token: dict[str, set[str]] = {}

# Keep track of (shared_token, state_token) pairs for each websocket connection (sid)
tokens_by_sid: dict[str, tuple[str, str]] = {}


class WhisperState(State):
    botmessage = ""
    clientmessage = ""
    # The clientToken is saved in the browser and identifies "shared" sessions
    clientToken: str = rx.Cookie("")
    task_output: str = ""

    # The messages is a special variable that is shared among all sessions with the same clientToken
    messages: list[dict] = []

    def ChangeBotMessage(self):
        self.messages.append({"role": "bot", "message": self.botmessage})

        # Apply changes to all other shared sessions
        return WhisperState.set_color_state_for_shared_sessions

    def ChangeClientMessage(self):
        self.messages.append({"role": "client", "message": self.clientmessage})

        # Apply changes to all other shared sessions
        return WhisperState.set_color_state_for_shared_sessions

    @rx.var
    def format_messages_for_client(self) -> list[str]:
        formatted_messages = []
        for message in self.messages:
            if message["role"] == "bot":
                formatted_messages.append([message["message"], "left", "#DEEAFD"])
            else:
                formatted_messages.append([message["message"], "right", "#F5EFFE"])
        return formatted_messages

    @rx.var
    def format_messages_for_bot(self) -> list[str]:
        formatted_messages = []
        for message in self.messages:
            if message["role"] == "bot":
                formatted_messages.append([message["message"], "right", "#F5EFFE"])
            else:
                formatted_messages.append([message["message"], "left", "#DEEAFD"])
        return formatted_messages

    async def set_color_state_for_shared_sessions(self):
        """Iterate through all shared sessions and update them with the new messages."""
        if not self.clientToken:
            self.set_client_token()

        print(f"{self.clientToken} -> {shared_sessions_by_token[self.clientToken]}")

        for token in shared_sessions_by_token.get(self.clientToken, set()):
            if token != self.get_token():
                async with app.modify_state(token) as other_state:
                    other_state.substates["whisper_state"].messages = self.messages

    async def set_color_state_for_new_session(self):
        """When a new session is created, copy the messages from another shared session."""
        for token in shared_sessions_by_token.get(self.clientToken, set()):
            if token != self.get_token():
                async with app.modify_state(token) as other_state:
                    self.messages = other_state.substates["whisper_state"].messages
                    return

    def set_client_token(self):
        """Page on_load handler uses the clientToken cookie to identify shared sessions."""
        if not self.clientToken:
            self.clientToken = self.get_token()

        # Mark this state's token as belonging to the clientToken
        shared_sessions_by_token.setdefault(self.clientToken, set()).add(
            self.get_token()
        )

        # Mark this state's websocket id as belonging to the clientToken and state token
        tokens_by_sid[self.get_sid()] = (self.clientToken, self.get_token())

        # Set the messages for the new session from existing shared sessions (if any)
        return WhisperState.set_color_state_for_new_session

    def interpret_last_question(self):
        client_messages = []
        for message in self.messages:
            if message["role"] == "client":
                client_messages.append(message["message"])

        documents = store.query(client_messages[-1])
        prompt = ragprompt(client_messages[-1], documents)
        response = llm(prompt)

        self.task_output = response

    def interpret_conversation(self):
        client_messages = []
        for message in self.messages:
            if message["role"] == "client":
                client_messages.append(message["message"])

        all_messages = " ".join(client_messages)

        documents = store.query(
            f"Can you interpret this client conversation {all_messages}"
        )
        prompt = ragprompt(
            f"Can you interpret this client conversation {all_messages}", documents
        )
        response = llm(prompt)

        self.task_output = response

    def summarise_conversation(self):
        client_messages = []
        for message in self.messages:
            client_messages.append(message["message"])

        all_messages = " ".join(client_messages)

        response = llm(f"Summarise this conversation {all_messages}")
        self.task_output = response

    def run_prompt(self):
        self.messages = [
            {
                "role": "client",
                "message": "Hey how's it going, I was hoping to get some help",
            },
            {"role": "bot", "message": "Sure what can I help you with?"},
            {
                "role": "client",
                "message": "I was hoping you can help me with watsonx.ai?",
            },
            {"role": "bot", "message": "Not an issue, what's the question?"},
            {"role": "client", "message": "Well, what is watsonx.ai?"},
        ]

    def clear_state(self):
        self.botmessage = ""
        self.clientmessage = ""
        self.task_output = ""
        self.messages = []


@rx.page(
    route="/whisperbot",
    title="WhisperBot - watsonx",
    on_load=WhisperState.set_client_token,
)
def page1() -> rx.Component:
    return rx.box(
        navbar(),
        rx.hstack(
            rx.container(
                rx.text(
                    """Want to use Generative AI to boost your agents? Simulate a client conversation by selecting Create Conversation. Then choose Interpret Last Question to get a response to the last client question. 
                    Want an overarching answer to your client query, hit Interpret Conversation or get a summary by choosing Summarise Conversation. Hit Clear when you're done.""",
                    color="#342E5C",
                    font_size="0.9em",
                    font_family=style.SANS,
                    padding_top="1em",
                ),
                rx.hstack(
                    rx.button(
                        "Create Conversation",
                        on_click=WhisperState.run_prompt,
                        style=style.PROMPT_BUTTON,
                    ),
                    rx.button(
                        "Clear",
                        on_click=WhisperState.clear_state,
                        style=style.CLEAR_BUTTON,
                    ),
                    style={"margin-top": "10px"},
                    position="sticky",
                    z_index="998",
                    top="0",
                ),
                chat_live_bot(WhisperState),
                action_bar_livechat(
                    WhisperState.set_botmessage, WhisperState.ChangeBotMessage
                ),
                height="100vh",
                display="flex",
                flex_direction="column",
                style={"min-width": "450px"},
            ),
            rx.container(
                rx.box(
                    rx.center(
                        rx.hstack(
                            rx.button(
                                "Interpret Last Question",
                                on_click=WhisperState.interpret_last_question,
                                style=style.PROMPT_BUTTON,
                            ),
                            rx.button(
                                "Interpret Conversation",
                                on_click=WhisperState.interpret_conversation,
                                style=style.PROMPT_BUTTON,
                            ),
                            rx.button(
                                "Summarise Conversation",
                                on_click=WhisperState.summarise_conversation,
                                style=style.PROMPT_BUTTON,
                            ),
                            style={"margin-top": "1em"},
                        )
                    ),
                    rx.cond(
                        WhisperState.task_output,
                        rx.center(
                            info_box("AI Generated Output", WhisperState.task_output),
                            rx.button(
                                "Copy to Clipboard",
                                on_click=rx.set_clipboard(WhisperState.task_output),
                                style=style.ASK_BUTTON,
                            ),
                        ),
                    ),
                ),
                height="100vh",
                display="flex",
                flex_direction="column",
                style={"min-width": "1000px"},
            ),
        ),
    )


@rx.page(
    route="/whisperclient",
    title="WhisperClient - watsonx",
    on_load=WhisperState.set_client_token,
)
def page2() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            chat_live_client(WhisperState),
            action_bar_livechat(
                WhisperState.set_clientmessage, WhisperState.ChangeClientMessage
            ),
            height="100vh",
            display="flex",
            flex_direction="column",
            style={"min-width": "450px"},
        ),
    )


# from app.client.whisper import shared_sessions_by_token, tokens_by_sid

# Add state and page to the app.
app = rx.App()
app.compile()

# Handle websocket disconnect events to avoid memory leaks when sessions are closed
orig_disconnect = app.event_namespace.on_disconnect


def disconnect_handler(sid):
    orig_disconnect(sid)

    clientToken, token = tokens_by_sid.get(sid, (None, None))
    print(
        f"Disconnect event received for {sid}. Removing {token} from shared {clientToken}"
    )

    shared_sessions_by_token.get(clientToken, set()).discard(token)
    tokens_by_sid.pop(sid, None)


app.event_namespace.on_disconnect = disconnect_handler
