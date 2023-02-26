import flet
from flet import *
import time
from math import pi

""" Inputs """

class UserInputField(UserControl):
    def __init__(self,icon_name,text_hint,hide):
        self.icon_name=icon_name
        self.text_hint=text_hint
        self.hide=hide
        super().__init__()

    def build(self):
        return Container(
            width=320, height=40,border=border.only(bottom=border.BorderSide(0.5,"white54")),
            content=Row(
                spacing=20,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(
                        name=self.icon_name,
                        size=14,
                        opacity=0.85
                    ),
                    TextField(
                        border_color="transparent",
                        bgcolor="transparent",
                        height=20,
                        width=200,
                        text_size=12,
                        content_padding=3,
                        cursor_color="white",
                        hint_text=self.text_hint,
                        hint_style=TextStyle(size=11),
                        password=self.hide,



                    )
                ]
            )
        )


""" Animations """


class AnimatedBox(UserControl):
    def __init__(self, border_color, bg_color, rotate_angle):
        self.border_color = border_color
        self.bg_color = bg_color
        self.rotate_angle = rotate_angle

    def build(self):
        return Container(
            width=48,
            height=48,
            border=border.all(2.5, self.border_color),
            bg_color=self.bg_color,
            border_radius=2,
            rotate=transform.Rotate(self.rotate_angle, alignment.center),
            animate_rotation=animation.Animation(700, "easeInOut")
        )


def main(page: Page):
    # dimensions
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "#1f262f"

    # main page controls
    page.add(
        Card(
            width=408,
            height=612,
            elevation=15,
            content=Container(
                bgcolor="#23262a",
                border_radius=6,
                content=Column(
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Divider(height=40, color='transparent'),
                        Stack(
                            controls=[

                            ]
                        ),
                        Divider(height=20, color="transparent"),
                        Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            alignment=MainAxisAlignment.CENTER,
                            spacing=5,
                            controls=[
                                Text("Sign In Below", size=22),
                                Text("Advanced python-flet UI Concepts", size=13)
                            ]
                        ),
                        Divider(height=20, color="transparent"),
                        UserInputField(icons.PERSON_ROUNDED,"Email",False),
                        Divider(height=20, color="transparent"),
                        UserInputField(icons.LOCK_OPEN_ROUNDED,"Password",True)
                    ]
                )
            )
        )
    )

    page.update()


if __name__ == "__main__":
    flet.app(target=main)
