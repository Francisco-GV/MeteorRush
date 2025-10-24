import arcade

from MeteorRush import constants
from MeteorRush.view.menu_view import MenuView


def main():
    window = arcade.Window(
        constants.SCREEN_WIDTH,
        constants.SCREEN_HEIGHT,
        constants.SCREEN_TITLE,
    )
    window.set_update_rate(1 / constants.MAX_FPS)

    arcade.load_font(":resources:/fonts/ttf/Kenney/Kenney_Future.ttf")

    arcade.enable_timings()

    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()
