import reflex as rx
from app.config import style
from app.components.navbar import navbar
from app.components.spline import spline_component

link_style = {
    "color": "black",
    "font_weight": style.BOLD_WEIGHT,
    "_hover": {"color": style.ACCENT_COLOR},
}


def container(*children, **kwargs):
    kwargs = {"max_width": "1440px", "padding_x": ["1em", "2em", "3em"], **kwargs}
    return rx.container(
        *children,
        **kwargs,
    )


def tag(text):
    return rx.text(
        text,
        color="#5646ED",
        bg="#F5EFFE",
        padding_x="0.5em",
        padding_y="0.25em",
        border_radius="8px",
        font_weight=600,
    )


def landing():
    return container(
        rx.hstack(
            rx.center(
                rx.vstack(
                    rx.text(
                        rx.span("[", color="#DACEEE"),
                        rx.span(".data", color="#696287"),
                        rx.span("]", color="#DACEEE"),
                        rx.span("[", color="#DACEEE"),
                        rx.span(".ai", color="#696287"),
                        rx.span("]", color="#DACEEE"),
                        rx.span("[", color="#DACEEE"),
                        rx.span(".governance", color="#696287"),
                        rx.span("]", color="#DACEEE"),
                        font_family=style.MONO,
                        mb=2,
                    ),
                    rx.text(
                        "Harness Generative AI in your business.",
                        font_family=style.MONO,
                        font_style="normal",
                        font_weight="600",
                        font_size="6xl",
                        line_height="1.2",
                        letter_spacing="-0.02em",
                    ),
                    rx.text(
                        "Automation, code generation and client engagement, you can do it faster and safer with watsonx.",
                        color="#342E5C",
                        font_size="1.1em",
                        font_family=style.SANS,
                        padding_top="1em",
                    ),
                    rx.cond(
                        True,
                        rx.wrap(
                            rx.input_group(
                                rx.input_left_element(
                                    rx.image(
                                        src="/landing_icons/custom_icons/email.png",
                                        height="1.2em",
                                    ),
                                ),
                                rx.input(
                                    placeholder="Your email address...",
                                    style=style.INPUT_STYLE,
                                    type="email",
                                ),
                                style=style.INPUT_STYLE,
                            ),
                            rx.button(
                                "Book a Risk Free POC Session",
                                style=style.ACCENT_BUTTON,
                            ),
                            justify="left",
                            should_wrap_children=True,
                            spacing="1em",
                            padding_x=".25em",
                            padding_y="1em",
                        ),
                        rx.text(
                            rx.icon(
                                tag="check",
                            ),
                            " You're on the waitlist!",
                            color=style.ACCENT_COLOR,
                        ),
                    ),
                    align_items="left",
                    padding="1em",
                ),
                width="100%",
            ),
            spline_component(),
        ),
        padding_top="6em",
        padding_bottom="6em",
        width="100%",
    )


def list_circle(text):
    return rx.flex(
        rx.text(text),
        width="2em",
        height="2em",
        border_radius="6px",
        bg="#F5EFFE",
        color="#5646ED",
        align_items="center",
        justify_content="center",
        font_weight="800",
    )


def example_card(title, tags, href, image):
    return rx.hstack(
        rx.image(src=image, height="1em", width="1em"),
        rx.text(title, color="#494369", font_weight="400"),
        rx.spacer(),
        *[tag(t) for t in tags],
        rx.link(
            rx.center(
                rx.icon(tag="arrow_forward", color="#494369"),
                border_radius="6px",
                box_shadow="0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14);",
                min_width="2em",
                min_height="2em",
            ),
            href=href,
        ),
        border="1px solid #F5EFFE",
        width="100%",
        padding=".5em",
        border_radius="8px",
    )


def intro():
    return rx.box(
        container(
            rx.text(
                "Empower Your Business with Generative AI.",
                font_size="4xl",
                font_family=style.MONO,
                font_style="normal",
                font_weight=600,
                pb=1,
                letter_spacing="-0.02em",
                mb=4,
            ),
            rx.text(
                "Harness the capabilities of watsonx for seamless AI integration. ",
                "Simplify the process of training, deploying, and leveraging AI.",
                color="#666",
                mb=8,
                max_width="50%",
            ),
            rx.flex(
                rx.box(
                    rx.hstack(
                        list_circle("1"),
                        rx.text("AI Training Simplified.", font_weight="600"),
                        mb=4,
                    ),
                    rx.text(
                        "watsonx provides intuitive tools for training your AI models, ensuring optimal performance.",
                        color="#666",
                        mb=4,
                    ),
                    rx.text(
                        rx.span('"""', color="#AA9EC3"),
                        rx.span(
                            "Experience the next-gen AI with watsonx!",
                            color="#494369",
                        ),
                        rx.span('"""', color="#AA9EC3"),
                        bg="#FAF8FB",
                        font_family=style.MONO,
                        p=4,
                        border="1px solid #EAE4FD",
                        mb=8,
                        border_radius="lg",
                    ),
                    rx.hstack(
                        list_circle("2"),
                        rx.text("Deploy & Scale.", font_weight="600"),
                        mb=4,
                    ),
                    rx.text(
                        "Deploy your AI models effortlessly and scale your business operations with watsonx.",
                        color="#666",
                    ),
                    flex=1,
                    margin_right=[0, 0, "1em"],
                    margin_bottom=["2em", "2em", 0],
                ),
                rx.vstack(
                    example_card(
                        "Generative Text",
                        ["NLP", "Content Generation"],
                        "https://github.com/watsonx-ai/watsonx-text",
                        "/landing_icons/custom_icons/chat.svg",
                    ),
                    example_card(
                        "Image Generation",
                        ["AI", "Visuals"],
                        "https://github.com/watsonx-ai/watsonx-images",
                        "/landing_icons/custom_icons/draw.svg",
                    ),
                    example_card(
                        "Predictive Analysis",
                        ["ML", "Forecasting"],
                        "https://github.com/watsonx-ai/watsonx-predict",
                        "/landing_icons/custom_icons/bucket.svg",
                    ),
                    example_card(
                        "Data Processing",
                        ["Automation", "Efficiency"],
                        "https://github.com/watsonx-ai/watsonx-data",
                        "/landing_icons/custom_icons/nodes.svg",
                    ),
                    align_items="center",
                    margin_left=[0, 0, "1em"],
                    flex=1,
                ),
                flex_direction=["column", "column", "column", "row", "row"],
            ),
        ),
        padding_top="5em",
        padding_bottom="5em",
    )


boxstyle = {}

aiTrainingBox = rx.hstack(
    rx.image(
        src="/landing_icons/icon1.svg",
        height="4em",
        width="4em",
    ),
    rx.vstack(
        rx.text(
            "AI Training Made Easy",
            font_size=style.H4_FONT_SIZE,
            font_weight=style.BOLD_WEIGHT,
        ),
        rx.text(
            "watsonx provides intuitive tools and resources to train your generative AI models efficiently.",
            color="#342E5C",
        ),
        rx.box(
            rx.link(
                rx.button(
                    "Explore AI Training Tools",
                    rx.icon(tag="arrow_forward"),
                    style=style.BUTTON_LIGHT_NO_BACKGROUND,
                    href="https://watsonx.com/ai-training",
                ),
                href="/docs/ai-training",
            )
        ),
        align_items="left",
        width="100%",
    ),
    style=boxstyle,
    align_items="left",
    spacing="1em",
    width="100%",
)

deploymentBox = rx.hstack(
    rx.image(
        src="/landing_icons/icon2.svg",
        height="4em",
        width="4em",
    ),
    rx.vstack(
        rx.text(
            "Seamless AI Deployment",
            font_size=style.H4_FONT_SIZE,
            font_weight=style.BOLD_WEIGHT,
        ),
        rx.text(
            "Deploy your trained AI models with watsonx's robust infrastructure, ensuring scalability and performance.",
            color="#342E5C",
        ),
        rx.box(
            rx.link(
                rx.button(
                    "Deployment Guide",
                    rx.icon(tag="arrow_forward"),
                    style=style.BUTTON_LIGHT_NO_BACKGROUND,
                ),
                href="/docs/ai-deployment",
            )
        ),
        align_items="left",
        width="100%",
    ),
    style=boxstyle,
    align_items="left",
    spacing="1em",
    width="100%",
)

integrationBox = rx.hstack(
    rx.image(
        src="/landing_icons/icon3.svg",
        height="4em",
        width="4em",
    ),
    rx.vstack(
        rx.text(
            "AI Integration Solutions",
            font_size=style.H4_FONT_SIZE,
            font_weight=style.BOLD_WEIGHT,
        ),
        rx.text(
            "Integrate watsonx's AI capabilities into your existing systems or applications with ease.",
            color="#342E5C",
        ),
        rx.box(
            rx.link(
                rx.button(
                    "Integration Guide",
                    rx.icon(tag="arrow_forward"),
                    style=style.BUTTON_LIGHT_NO_BACKGROUND,
                ),
                href="/docs/ai-integration",
            )
        ),
        align_items="left",
        width="100%",
    ),
    style=boxstyle,
    align_items="left",
    spacing="1em",
    width="100%",
)

leverageAIBox = rx.hstack(
    rx.image(
        src="/landing_icons/icon4.svg",
        height="4em",
        width="4em",
    ),
    rx.vstack(
        rx.text(
            "Leverage AI for Business Growth",
            font_size=style.H4_FONT_SIZE,
            font_weight=style.BOLD_WEIGHT,
        ),
        rx.text(
            "Discover how watsonx can transform your business operations, drive innovation, and enhance customer experiences.",
            color="#342E5C",
        ),
        align_items="left",
        width="100%",
    ),
    style=boxstyle,
    align_items="left",
    spacing="1em",
    width="100%",
)


def ai_platform():
    return rx.box(
        container(
            height="8em",
            width="100%",
            background="radial-gradient(55.39% 67.5% at 50% 100%, rgba(188, 136, 255, 0.16) 0%, rgba(255, 255, 255, 0) 100%);",
            opacity="0.4;",
            transform="matrix(1, 0, 0, -1, 0, 0);",
        ),
        container(
            rx.vstack(
                rx.box(
                    rx.text(
                        "[",
                        rx.span("watsonx", bg="#F5EFFE", color="#5646ED"),
                        "]",
                        color="#5646ED",
                        font_family=style.MONO,
                    )
                ),
                rx.heading(
                    "Empower Your Business with Generative AI.",
                    font_size=style.H3_FONT_SIZE,
                    font_family=style.MONO,
                ),
                rx.text(
                    "Train, deploy, and leverage AI seamlessly. watsonx is your all-in-one platform for generative AI solutions.",
                    color="#342E5C",
                    max_width="50%",
                ),
                rx.hstack(
                    rx.desktop_only(
                        rx.vstack(
                            rx.hstack(
                                aiTrainingBox,
                                deploymentBox,
                                spacing="2em",
                                height="100%",
                            ),
                            rx.hstack(
                                integrationBox,
                                leverageAIBox,
                                height="100%",
                                spacing="2em",
                            ),
                            padding_bottom="2em",
                            width="100%",
                            spacing="2em",
                        )
                    ),
                    rx.mobile_and_tablet(
                        rx.vstack(
                            aiTrainingBox,
                            deploymentBox,
                            integrationBox,
                            leverageAIBox,
                            padding_bottom="2em",
                            height="100%",
                            spacing="2em",
                        )
                    ),
                    padding_y="2em",
                ),
                padding_bottom="2em",
                align_items="left",
            )
        ),
        bg="rgba(247, 247, 250, 0.6);",
    )


def ai_platform_backend():
    return rx.box(
        container(
            height="8em",
            width="100%",
            background="radial-gradient(55.39% 67.5% at 50% 100%, #EBEBFF 0%, rgba(255, 255, 255, 0) 100%)",
            opacity="0.4;",
            transform="matrix(1, 0, 0, -1, 0, 0);",
        ),
        container(
            rx.vstack(
                rx.box(
                    rx.text(
                        "[",
                        rx.span("watsonx Backend", color="#2B199C", bg="#F3F7FE"),
                        "]",
                        color="#2B199C",
                        font_family=style.MONO,
                    )
                ),
                rx.heading(
                    "Seamless AI Integration and Deployment",
                    font_size=style.H3_FONT_SIZE,
                    font_family=style.MONO,
                ),
                rx.text(
                    "watsonx provides a robust backend infrastructure optimized for generative AI applications.",
                    color="#342E5C",
                    max_width="50%",
                ),
                rx.hstack(
                    rx.desktop_only(
                        rx.vstack(
                            rx.hstack(
                                ai_deploy_icon,
                                ai_host_icon,
                                spacing="2em",
                                height="100%",
                            ),
                            padding_bottom="2em",
                            width="100%",
                            spacing="2em",
                            align_items="left",
                        )
                    ),
                    rx.mobile_and_tablet(
                        rx.vstack(
                            ai_deploy_icon,
                            ai_host_icon,
                            padding_bottom="2em",
                            height="100%",
                            spacing="2em",
                        )
                    ),
                    padding_y="2em",
                ),
                padding_bottom="2em",
                align_items="left",
            )
        ),
        bg="rgba(247, 247, 250, 0.6);",
    )


ai_deploy_icon = rx.hstack(
    rx.image(
        src="/landing_icons/battery-icon.svg",
        height="4em",
        width="4em",
    ),
    rx.vstack(
        rx.text(
            "AI Model Deployment",
            font_size=style.H4_FONT_SIZE,
            font_weight=style.BOLD_WEIGHT,
        ),
        rx.text(
            "Deploy your trained AI models effortlessly with watsonx's advanced backend solutions.",
            color="#342E5C",
        ),
        rx.box(
            rx.link(
                rx.button(
                    "AI Deployment Guide",
                    rx.icon(tag="arrow_forward"),
                    style=style.BUTTON_LIGHT_NO_BACKGROUND,
                ),
                href="/docs/ai-platform/deploy",
            )
        ),
        align_items="left",
        width="100%",
    ),
    style=boxstyle,
    align_items="left",
    spacing="1em",
    width="100%",
)

ai_host_icon = rx.hstack(
    rx.image(
        src="/landing_icons/orm-icon.svg",
        height="4em",
        width="4em",
    ),
    rx.vstack(
        rx.text(
            "Self-host Your AI Solutions",
            font_size=style.H4_FONT_SIZE,
            font_weight=style.BOLD_WEIGHT,
        ),
        rx.text(
            "With watsonx, you have the flexibility to host your AI solutions on-premises or on your preferred cloud.",
            color="#342E5C",
        ),
        rx.box(
            rx.link(
                rx.button(
                    "Self-hosting Guide",
                    rx.icon(tag="arrow_forward"),
                    style=style.BUTTON_LIGHT_NO_BACKGROUND,
                ),
                href="/docs/ai-platform/self-hosting",
            )
        ),
        align_items="left",
        width="100%",
    ),
    style=boxstyle,
    align_items="left",
    spacing="1em",
    width="100%",
)


def format_with_commas(number):
    return "{:,}+".format(number)


def prompt_sign():
    return rx.text(
        "$",
        color=style.ACCENT_COLOR,
        font_family=style.SANS,
        style={"userSelect": "none"},
    )


def ai_installation():
    return rx.vstack(
        container(
            rx.flex(
                rx.center(
                    rx.vstack(
                        rx.heading(
                            "Kickstart Your AI Journey with watsonx!",
                            font_family=style.MONO,
                            font_weight=style.BOLD_WEIGHT,
                            font_size=style.H3_FONT_SIZE,
                        ),
                        rx.box(
                            rx.text(
                                "watsonx is compatible with Python 3.7+",
                            ),
                            color="#82799E",
                            font_family=style.SANS,
                            padding_y=".5em",
                        ),
                        align_items="start",
                        min_width="10em",
                        margin_x="auto",
                        width="100%",
                    ),
                    min_width="10em",
                    width="100%",
                    mb=8,
                ),
                rx.vstack(
                    rx.text(
                        "Follow these steps to set up watsonx:",
                        font_family=style.MONO,
                        padding_x="1em",
                        padding_top=".5em",
                    ),
                    rx.divider(),
                    rx.vstack(
                        rx.hstack(
                            rx.text("1", color="#494369"),
                            prompt_sign(),
                            rx.text(
                                "pip install watsonx",
                                font_family=style.MONO,
                                font_weight="500",
                            ),
                        ),
                        rx.hstack(
                            rx.text("2", color="#494369"),
                            prompt_sign(),
                            rx.text(
                                "watsonx initialize",
                                font_family=style.MONO,
                                font_weight="500",
                            ),
                        ),
                        rx.hstack(
                            rx.text("3", color="#494369"),
                            prompt_sign(),
                            rx.text(
                                "watsonx deploy",
                                font_family=style.MONO,
                                font_weight="500",
                            ),
                        ),
                        width="100%",
                        align_items="left",
                        padding_x="1em",
                    ),
                    rx.divider(),
                    rx.hstack(
                        rx.text(
                            "Congratulations! You've just set up your first generative AI with watsonx.",
                        ),
                        rx.spacer(),
                        rx.link(
                            rx.button(
                                "AI Documentation",
                                style=style.ACCENT_BUTTON,
                                padding_x="1em",
                            ),
                            href="/docs/ai-platform/introduction",
                            style=style.NAV_TEXT_STYLE,
                        ),
                        width="100%",
                        padding=4,
                    ),
                    height="100%",
                    border="1px solid #342E5C;",
                    box_shadow="0px 2px 3px rgba(3, 3, 11, 0.32), 0px 4px 8px rgba(3, 3, 11, 0.32), 0px 4px 10px -2px rgba(3, 3, 11, 0.52), inset 0px 1px 0px rgba(255, 255, 255, 0.16), inset 0px 20px 32px -10px rgba(86, 70, 237, 0.32);",
                    bg="radial-gradient(69.66% 165.73% at 70.23% 84.65%, rgba(86, 70, 237, 0.12) 0%, rgba(20, 18, 39, 0.12) 100%) /* warning: gradient uses a rotation that is not supported by CSS and may not behave as expected */, #110F1F;",
                    border_radius="8px;",
                    align_items="left",
                    width="100%",
                    min_width="25em",
                ),
                width="100%",
                flex_direction=["column", "column", "column", "column", "row"],
            ),
            width="100%",
        ),
        rx.box(
            height="5em",
            width="100%",
            background="radial-gradient(55.39% 67.5% at 50% 100%, rgba(188, 136, 255, 0.16) 0%, rgba(255, 255, 255, 0) 100%);",
            opacity="0.75;",
        ),
        font_family=style.SANS,
        color="white",
        width="100%",
        bg="#110F1F",
        padding_top="2em",
        display=["none", "flex", "flex", "flex", "flex"],
    )


@rx.page(route="/", title="watsonx Walkthrough")
def index() -> rx.Component:
    """Get the main Reflex landing page."""
    return rx.box(
        navbar(),
        landing(),
        container(rx.divider(border_color="#F4F3F6")),
        intro(),
        ai_platform(),
        ai_platform_backend(),
        ai_installation(),
        width="100%",
    )
