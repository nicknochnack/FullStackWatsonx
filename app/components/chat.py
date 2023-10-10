import reflex as rx
from app.config import style


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(rx.text(question, style=style.question_style), text_align="right"),
        rx.box(rx.text(answer, style=style.answer_style), text_align="left"),
        margin_y="1em",
    )


def chat(state) -> rx.Component:
    return rx.box(
        rx.foreach(state.chat_history, lambda messages: qa(messages[0], messages[1])),
        flex="1",  # This allows the chat box to take up all available space
    )


def action_bar(state) -> rx.Component:
    # Updated input style for a larger and wider appearance
    larger_input_style = {
        **style.input_style,
        "height": "50px",
        "fontSize": "18px",
        "padding": "10px",
        "min-width": "450px",
    }

    return rx.hstack(
        rx.input(
            placeholder="Ask a question",
            value=state.question,
            on_blur=state.set_question,
            style=larger_input_style,
            on_change=state.set_question,
        ),
        rx.button("Ask", on_click=state.answer, style=style.ASK_BUTTON),
        position="sticky",  # Make the action bar sticky
        bottom="0",  # Stick it to the bottom
        background="white",  # Ensure it has a background to overlay content
        padding_bottom="100px",  # Add padding below the action bar
    )


def qa_live(message: list) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(
                message[0],
                style=dict(
                    padding="1em",
                    border_radius="5px",
                    margin_y="0.5em",
                    box_shadow="rgba(0, 0, 0, 0.15) 0px 2px 8px",
                    # max_width="30em",
                    display="inline-block",
                ),
                bg=message[2],
            ),
            text_align=message[1],
        ),
        margin_y="1em",
    )


def chat_live_client(state) -> rx.Component:
    return rx.box(
        rx.foreach(state.format_messages_for_client, lambda message: qa_live(message)),
        flex="1",  # This allows the chat box to take up all available space
    )


def chat_live_bot(state) -> rx.Component:
    return rx.box(
        rx.foreach(state.format_messages_for_bot, lambda message: qa_live(message)),
        flex="1",  # This allows the chat box to take up all available space
    )


def action_bar_livechat(message_function, send_function) -> rx.Component:
    # Updated input style for a larger and wider appearance
    larger_input_style = {
        **style.input_style,
        "height": "50px",
        "fontSize": "18px",
        "padding": "10px",
        "min-width": "450px",
    }

    return rx.hstack(
        rx.input(
            placeholder="Ask a question",
            on_blur=message_function,
            style=larger_input_style,
        ),
        rx.button("Ask", on_click=send_function, style=style.ASK_BUTTON),
        position="sticky",  # Make the action bar sticky
        bottom="0",  # Stick it to the bottom
        background="white",  # Ensure it has a background to overlay content
        padding_bottom="100px",  # Add padding below the action bar
    )
