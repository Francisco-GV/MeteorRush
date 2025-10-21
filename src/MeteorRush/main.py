import arcade

from MeteorRush.constants import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH
from MeteorRush.view.menu_view import MenuView


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()
