import reflex as rx
from app.config import style


def info_box(heading: str, content: str) -> rx.Component:
    return rx.box(
        # rx.container(
        #     height="8em",
        #     width="100%",
        #     background="radial-gradient(55.39% 67.5% at 50% 100%, rgba(188, 136, 255, 0.16) 0%, rgba(255, 255, 255, 0) 100%);",
        #     opacity="0.4;",
        #     transform="matrix(1, 0, 0, -1, 0, 0);",
        # ),
        rx.container(
            rx.box(
                rx.text(
                    heading,
                    font_size="4xl",
                    font_family=style.MONO,
                    font_style="normal",
                    font_weight=600,
                    pb=1,
                    letter_spacing="-0.02em",
                    mb=4,
                ),
            ),
            rx.text(
                content,
                color="#342E5C",
            ),
            # bg_color="lightblue",  # Light blue background color
            color="darkblue",  # Dark blue text color
            box_shadow="0px 4px 6px rgba(0, 0, 0, 0.1)",  # Drop shadow
            padding="1em",  # Padding for better appearance
            border_radius="0.5em",  # Rounded corners
            margin="1em",  # Margin for better appearance
            border="1px dashed #c44d56",
            width="100%",
        ),
    )
