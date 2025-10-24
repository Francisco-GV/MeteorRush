import arcade
from arcade.gui import (UIAnchorLayout, UIBoxLayout, UIFlatButton, UILabel,
                        UIManager)

from MeteorRush.utils import scale_and_center_background
from MeteorRush.view.game_view import GameView


class MenuView(arcade.View):
    def __init__(self):
        super().__init__()

        self.background_list = None
        self.setup()

    def setup(self):
        self.background_list = arcade.SpriteList()

        background_sprite = scale_and_center_background(
            "assets/images/backgrounds/Green_Nebula_07-1024x1024.png"
        )

        self.background_list.append(background_sprite)

    def on_show_view(self):
        self.manager = UIManager()
        self.manager.enable()

        self.v_box = UIBoxLayout()

        title_label = UILabel(
            text="Meteor Rush",
            font_size=50,
            font_name="Kenney Future",
            text_color=arcade.color.WHITE,
        )

        self.v_box.add(title_label.with_padding(bottom=50))

        start_button: UIFlatButton = UIFlatButton(text="Iniciar Juego", width=250)
        self.v_box.add(start_button.with_padding(bottom=20))

        quit_button: UIFlatButton = UIFlatButton(text="Salir", width=250)
        self.v_box.add(quit_button.with_padding(bottom=20))

        start_button.on_click = self.on_click_start
        quit_button.on_click = self.on_click_quit

        anchor_layout = UIAnchorLayout()
        anchor_layout.add(
            child=self.v_box,
            anchor_x="center",
            anchor_y="center",
        )

        self.manager.add(anchor_layout)

    def on_hide_view(self):
        self.manager.disable()

    def on_click_start(self, event):
        game_view = GameView()
        self.window.show_view(game_view)

    def on_click_quit(self, event):
        arcade.exit()

    def on_draw(self):
        self.clear()

        if self.background_list:
            self.background_list.draw()

        self.manager.draw()
