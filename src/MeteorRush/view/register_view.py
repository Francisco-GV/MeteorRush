import arcade
from arcade.gui import (UIAnchorLayout, UIBoxLayout, UIFlatButton, UIInputText,
                        UILabel, UIManager)

from MeteorRush.view.game_view import GameView


class RegisterView(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = UIManager()
        self.v_box = UIBoxLayout()
        self.background_list = arcade.SpriteList()

        self.background_sprite = arcade.Sprite(
            "assets/images/backgrounds/Purple_Nebula_06-1024x1024.png"
        )
        self.background_sprite.center_x = self.window.width / 2
        self.background_sprite.center_y = self.window.height / 2
        self.background_list.append(self.background_sprite)

        title_label = UILabel(
            text="Regístrate",
            font_size=50,
            font_name="Kenney Future",
            text_color=arcade.color.WHITE,
        )
        self.v_box.add(title_label.with_padding(bottom=50))

        self.name_input = UIInputText(
            text=" ",
            width=250,
            height=64,
            font_size=24,
            font_name="Kenney Future",
            text_color=arcade.color.WHITE,
        )
        self.v_box.add(self.name_input.with_padding(all=10))

        start_button = UIFlatButton(
            text="Iniciar",
            width=250,
        )

        self.v_box.add(start_button.with_padding(top=20))

        start_button.on_click = self.on_click_start

        anchor_layout = UIAnchorLayout()
        anchor_layout.add(
            child=self.v_box,
            anchor_x="center",
            anchor_y="center",
        )
        self.manager.add(anchor_layout)

    def on_show_view(self):
        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()

    def on_click_start(self, event):
        player_name = self.name_input.text

        if player_name and player_name.strip():
            game_view = GameView()
            game_view.player_name = player_name
            self.window.show_view(game_view)

    def on_draw(self):
        self.clear()
        self.background_list.draw()
        self.manager.draw()
