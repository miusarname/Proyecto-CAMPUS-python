import flet
from flet import *
import time
from math import pi

"""Animations """


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
                               AnimatedBox("#e9665a","#23262a" ,0),
                               AnimatedBox("#7df6dd","#23262a",10 )
                            ]
                        )
                    ]
                )
            )
        )
    )

    page.update()


if __name__ == "__main__":
    flet.app(target=main)
