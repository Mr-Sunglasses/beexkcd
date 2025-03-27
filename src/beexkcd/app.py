"""
xkcd gui reader written in beeware.
"""

import toga
from toga import Image, ImageView
from toga.fonts import SANS_SERIF
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

from .xkcd import XKCD

myXCD = XKCD()


class beexkcd(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """

        main_box = toga.Box(style=Pack(direction=COLUMN))

        self.my_label = toga.Label(
            myXCD.get_title,
            style=Pack(padding=(60, 140), font_size=25, font_family=SANS_SERIF),
        )
        main_box.add(self.my_label)

        btn_previous = toga.Button(
            "Previous", on_press=self.previous_image, style=Pack(padding=10)
        )

        btn_random = toga.Button(
            "Random", on_press=self.random_image, style=Pack(padding=10)
        )

        btn_next = toga.Button("Next", on_press=self.next_image, style=Pack(padding=10))

        main_box.add(btn_previous, btn_random, btn_next)

        self.my_img = toga.images.Image(src=myXCD.get_image_data)
        self.img = toga.ImageView(image=self.my_img)
        # main_box.add(self.img)

        image_box = toga.Box(style=Pack(direction=ROW, padding=50))
        image_box.add(self.img)

        main_box.add(image_box)

        container = toga.ScrollContainer(content=main_box)

        self.main_window = toga.MainWindow(title=myXCD.get_title)
        # self.main_window.content = main_box
        self.main_window.content = container
        self.main_window.show()

    def next_image(self, widget):
        myXCD.next

        # Update the image
        self.my_img = toga.images.Image(src=myXCD.get_image_data)
        self.img.image = self.my_img

        # Update the title
        self.my_label.text = myXCD.get_title

        # Update the window title
        self.main_window.title = myXCD.get_title

    def previous_image(self, widget):
        myXCD.previous

        # Update the image
        self.my_img = toga.images.Image(src=myXCD.get_image_data)
        self.img.image = self.my_img

        # Update the title
        self.my_label.text = myXCD.get_title

        # Update the window title
        self.main_window.title = myXCD.get_title

    def random_image(self, widget):
        myXCD.random

        # Update the image
        self.my_img = toga.images.Image(src=myXCD.get_image_data)
        self.img.image = self.my_img

        # Update the title
        self.my_label.text = myXCD.get_title

        # Update the window title
        self.main_window.title = myXCD.get_title


def main():
    return beexkcd()
