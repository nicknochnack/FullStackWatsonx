import reflex as rx
from reflex.vars import Var


class Spline(rx.Component):
    """Spline component."""

    library = "@splinetool/react-spline"
    tag = "Spline"
    scene: Var[str] = "https://prod.spline.design/Gjwu-bLJSqolGAtm/scene.splinecode"
    # scene: Var[str] = "https://prod.spline.design/QKYR4OyTzTmuaTg2/scene.splinecode"

    is_default = True

    lib_dependencies: list[str] = ["@splinetool/runtime"]


spline = Spline.create


def spline_component():
    return rx.center(
        rx.center(
            spline(),
            overflow="hidden",
            width="42em",
            height="42em",
        ),
        width="100%",
        display=["none", "none", "none", "none", "flex", "flex"],
    )
