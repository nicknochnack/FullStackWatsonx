"""UI and logic for the navbar component."""
from typing import Any, Set

import reflex as rx
from app.config import style
from app.components.logo import navbar_logo


def shorten_to_k(number):
    if number >= 1000:
        return "{:.0f}k+".format(number / 1000)
    else:
        return str(number)


# Style to use for the navbar.
logo_style = {
    "height": "1.25em",
}
logo = navbar_logo(**logo_style)


hover_button_style = {
    "_hover": {
        "background": "radial-gradient(82.06% 100% at 50% 100%, rgba(91, 77, 182, 0.04) 0%, rgba(234, 228, 253, 0.2) 100%), #FEFEFF;",
        "boxShadow": "0px 0px 0px 3px rgba(149, 128, 247, 0.6), 0px 2px 3px rgba(3, 3, 11, 0.2), 0px 4px 8px rgba(3, 3, 11, 0.04), 0px 4px 10px -2px rgba(3, 3, 11, 0.02), inset 0px 2px 0px rgba(255, 255, 255, 0.01), inset 0px 0px 0px 1px rgba(32, 17, 126, 0.4), inset 0px -20px 12px -4px rgba(234, 228, 253, 0.36);",
    },
}


def github_button():
    return rx.link(
        rx.hstack(
            rx.image(src="/companies/dark/github.svg", height="1.25em"),
            rx.text("Star", style=style.NAV_TEXT_STYLE),
            rx.text(
                shorten_to_k(120000),
                color="#5646ED",
                bg="#F5EFFE",
                padding_x="0.5em",
                border_radius="6px",
                font_weight=600,
            ),
            box_shadow="0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14);",
            padding_x=".5em",
            height="2em",
            border_radius="8px",
            bg="#FFFFFF",
            style=hover_button_style,
        ),
        href="https://ibm.com",
        display=["none", "none", "none", "flex", "flex", "flex"],
    )


def discord_button():
    return rx.link(
        rx.center(
            rx.image(src="/companies/dark/discord.svg", height="1.25em"),
            box_shadow="0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14);",
            display=["none", "none", "none", "flex", "flex", "flex"],
            height="2em",
            width="2em",
            border_radius="8px",
            bg="#FFFFFF",
            style=hover_button_style,
        ),
        href="https://ibm.com",
    )


def navbar() -> rx.Component:
    """Create the navbar component.

    Args:
        sidebar: The sidebar component to use.
    """

    # Create the navbar component.
    return rx.vstack(
        rx.box(
            rx.hstack(
                rx.hstack(
                    logo,
                    rx.link(
                        "Docs",
                        href="https://dataplatform.cloud.ibm.com/docs/content/?context=wx",
                        style=style.NAV_TEXT_STYLE,
                        display=["none", "none", "none", "flex", "flex", "flex"],
                    ),
                    rx.link(
                        "Blog",
                        href="https://www.ibm.com/blog/tag/watsonx/",
                        style=style.NAV_TEXT_STYLE,
                        display=["none", "none", "none", "flex", "flex", "flex"],
                    ),
                    rx.link(
                        "Tutorials",
                        href="https://developer.ibm.com/components/watsonx/tutorials",
                        style=style.NAV_TEXT_STYLE,
                        display=["none", "none", "none", "none", "flex", "flex"],
                    ),
                    rx.menu(
                        rx.menu_button(
                            rx.hstack(
                                rx.text("Stories", style=style.NAV_TEXT_STYLE),
                                rx.icon(tag="chevron_down", style=style.NAV_TEXT_STYLE),
                                cursor="pointer",
                                display=[
                                    "flex",
                                    "flex",
                                    "flex",
                                ],
                            )
                        ),
                        rx.menu_list(
                            rx.link(
                                rx.menu_item(
                                    "Code Generation", style=style.NAV_DROPDOWN_STYLE
                                ),
                                href="/codegen",
                            ),
                            rx.link(
                                rx.menu_item(
                                    "Client Discovery", style=style.NAV_DROPDOWN_STYLE
                                ),
                                href="/clientdiscovery",
                            ),
                            rx.link(
                                rx.menu_item(
                                    "Whisper Bot", style=style.NAV_DROPDOWN_STYLE
                                ),
                                href="/whisperbot",
                            ),
                            # rx.menu_divider(),
                        ),
                    ),
                    rx.menu(
                        rx.menu_button(
                            rx.hstack(
                                rx.text("Products", style=style.NAV_TEXT_STYLE),
                                rx.icon(tag="chevron_down", style=style.NAV_TEXT_STYLE),
                                cursor="pointer",
                                display=[
                                    "none",
                                    "none",
                                    "none",
                                    "flex",
                                    "flex",
                                    "flex",
                                ],
                            )
                        ),
                        rx.menu_list(
                            rx.link(
                                rx.menu_item(
                                    "watsonx.ai", style=style.NAV_DROPDOWN_STYLE
                                ),
                                href="/docs/gallery",
                            ),
                            rx.link(
                                rx.menu_item(
                                    "watsonx.data", style=style.NAV_DROPDOWN_STYLE
                                ),
                                href="https://ibm.com",
                            ),
                            rx.link(
                                rx.menu_item(
                                    "watsonx.governance", style=style.NAV_DROPDOWN_STYLE
                                ),
                                href="/faq",
                            ),
                            rx.link(
                                rx.menu_item(
                                    "watsonx Assistant", style=style.NAV_DROPDOWN_STYLE
                                ),
                                href="/faq",
                            ),
                            rx.link(
                                rx.menu_item(
                                    "watsonx Orchestrate",
                                    style=style.NAV_DROPDOWN_STYLE,
                                ),
                                href="/faq",
                            ),
                            rx.link(
                                rx.menu_item(
                                    "watsonx Code Assistant",
                                    style=style.NAV_DROPDOWN_STYLE,
                                ),
                                href="/faq",
                            ),
                            # rx.menu_divider(),
                        ),
                    ),
                    spacing="2em",
                ),
                rx.hstack(
                    github_button(),
                    discord_button(),
                    rx.icon(
                        tag="hamburger",
                        width="1.5em",
                        height="1.5em",
                        _hover={
                            "cursor": "pointer",
                            "color": style.ACCENT_COLOR,
                        },
                        display=["flex", "flex", "flex", "none", "none", "none"],
                    ),
                    height="full",
                ),
                justify="space-between",
                padding_x=style.PADDING_X,
            ),
            bg="rgba(255,255,255, 0.9)",
            backdrop_filter="blur(10px)",
            padding_y=["0.8em", "0.8em", "0.5em"],
            border_bottom="1px solid #F4F3F6",
            width="100%",
        ),
        position="sticky",
        z_index="999",
        top="0",
        width="100%",
        spacing="0",
    )
