import arcade


class MenuView(arcade.View):

    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)

    def on_draw(self):
        self.clear()

        arcade.draw_text(
            "Meteor Rush",
            self.window.width / 2,
            self.window.height / 2 + 50,
            arcade.color.WHITE,
            font_size=50,
            anchor_x="center",
        )

        arcade.draw_text(
            "Presiona ENTER para comenzar",
            self.window.width / 2,
            self.window.height / 2 - 50,
            arcade.color.LIGHT_GRAY,
            font_size=20,
            anchor_x="center",
        )
