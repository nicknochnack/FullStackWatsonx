import reflex as rx

# Import app components
from app.components.navbar import navbar
from app.components.chat import chat, action_bar

# Load overall application state
from app.config.state import State
from app.config import style

# Import Starcoder and use base chain
from app.utils.watsonxga import WatsonxLangchainLLM
from app.utils.watsonxworkbench import WatsonxWorkbenchLangchainLLM
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

from app.config.state import State

config = rx.config.get_config()

if config.watsonx_type == "ga":
    # Create Starcoder chain
    llm = WatsonxLangchainLLM(
        model_id=ModelTypes.STARCODER.value,
        generate_params={
            GenParams.DECODING_METHOD: "greedy",
            GenParams.MAX_NEW_TOKENS: 200,
        },
    ).from_pretrained()

if config.watsonx_type == "workbench":
    llm = WatsonxWorkbenchLangchainLLM(
        model_id="codellama/codellama-34b-instruct",
        generate_params={
            GenParams.DECODING_METHOD: "greedy",
            GenParams.MAX_NEW_TOKENS: 200,
            "stream": True,
        },
    ).from_pretrained()


class CodeGenState(State):
    """The page state."""

    question: str = ""
    code_history: str
    chat_history: list[tuple[str, str]]

    async def answer(self):
        if config.watsonx_type == "ga":
            answer = llm(self.question)
            self.code_history += str(answer)
            self.chat_history.append((self.question, answer))
            self.question = ""

        if config.watsonx_type == "workbench":
            history = "\n ".join(
                [f"Q:{chat[0]} H:{chat[1]}" for chat in self.chat_history]
            )
            prompt = starcoder_template(history, self.question)
            self.chat_history.append((self.question, ""))
            answer = ""
            for response in llm.stream(prompt):
                answer += response
                self.code_history += str(response)
                self.chat_history[-1] = (self.question, answer)
                yield
            self.question = ""

    def run_prompt(self, prompt):
        self.question = prompt

    def clear_state(self):
        self.question = ""
        self.code_history = ""
        self.chat_history = []


def starcoder_template(history, prompt):
    return f"[inst]<sys>You are a coding assistant.</sys> This is a summary of the previous interactions. {history} Try to help answer the following:{prompt} [\inst]"


def codeblock() -> rx.Component:
    return rx.cond(
        CodeGenState.code_history,
        rx.code_block(
            CodeGenState.code_history, language="python", show_line_numbers=True
        ),
    )


@rx.page(route="/codegen", title="Code Generation - watsonx")
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.hstack(
            rx.container(
                rx.text(
                    "Try out code generation below. Select one of the prompts e.g. Import Data then hit ask to generate code. Hit Clear once you're done.",
                    color="#342E5C",
                    font_size="0.9em",
                    font_family=style.SANS,
                    padding_top="1em",
                ),
                rx.hstack(
                    rx.button(
                        "Import Data",
                        on_click=lambda: CodeGenState.run_prompt(
                            "Import data from a file called data.csv and show the first five rows."
                        ),
                        style=style.PROMPT_BUTTON,
                    ),
                    rx.button(
                        "Build Linear Model",
                        on_click=lambda: CodeGenState.run_prompt(
                            "Build a linear model using scikit-learn."
                        ),
                        style=style.PROMPT_BUTTON,
                    ),
                    rx.button(
                        "Export to Joblib",
                        on_click=lambda: CodeGenState.run_prompt(
                            "Export the model using joblib"
                        ),
                        style=style.PROMPT_BUTTON,
                    ),
                    rx.button(
                        "Clear",
                        on_click=CodeGenState.clear_state,
                        style=style.CLEAR_BUTTON,
                    ),
                    style={"margin-top": "10px"},
                    position="sticky",
                    z_index="998",
                    top="0",
                ),
                rx.vstack(
                    chat(CodeGenState),
                    action_bar(CodeGenState),
                    height="100vh",
                    display="flex",
                    flex_direction="column",
                ),
                style={"min-width": "450px"},
            ),
            rx.container(
                rx.vstack(
                    rx.center(
                        rx.button(
                            "Copy to Clipboard",
                            on_click=rx.set_clipboard(CodeGenState.code_history),
                            style=style.ASK_BUTTON,
                        )
                    ),
                    codeblock(),
                    height="100vh",
                    display="inline-block",
                    # flex_direction="column",
                    style={
                        "inline-size": "800px",
                        "overflow-wrap": "break-word",
                    },
                ),
                style={"min-width": "1000px"},
            ),
        ),
    )
