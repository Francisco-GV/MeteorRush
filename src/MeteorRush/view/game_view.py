import math

import arcade

from MeteorRush import constants
from MeteorRush.sprites.player import Player


class GameView(arcade.View):

    def __init__(self):
        super().__init__()
        self.player = None
        self.player_list = None
        self.bullet_list = None
        self.ammo_texture = None

        self.up_pressed = False
        self.down_pressed = False

        self.left_pressed = False
        self.right_pressed = False

    def setup(self):
        self.player = Player()
        self.player_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.player_list.append(self.player)

        if self.player:
            self.ammo_texture = arcade.load_texture(
                self.player.weapon.bullet_texture_path
            )

    def on_show_view(self):
        arcade.set_background_color(arcade.color.AMAZON)
        self.setup()

    def on_draw(self):
        self.clear()

        if self.bullet_list:
            self.bullet_list.draw()

        if self.player_list:
            self.player_list.draw()

        if self.player and self.ammo_texture:
            ammo_start_x = self.ammo_texture.width + 15
            ammo_start_y = self.ammo_texture.height + 5
            ammo_spacing = 15
            ammo_scale = 0.8

            scaled_width = self.ammo_texture.width * ammo_scale
            scaled_height = self.ammo_texture.height * ammo_scale

            weapon = self.player.weapon

            i = 0
            while i < weapon.magazine_size:
                center_x = ammo_start_x + i * ammo_spacing
                center_y = ammo_start_y
                bottom_left_x = center_x - (scaled_width / 2)
                bottom_left_y = center_y - (scaled_height / 2)

                arcade.draw_texture_rect(
                    texture=self.ammo_texture,
                    rect=arcade.XYWH(
                        x=bottom_left_x,
                        y=bottom_left_y,
                        width=scaled_width,
                        height=scaled_height,
                    ),
                    alpha=255 if i < weapon.current_ammo else 100
                )

                i += 1

        fps = arcade.get_fps()
        arcade.draw_text(
            f"FPS: {fps:.0f}",
            10,
            self.window.height - 30,
            arcade.color.WHITE,
            18,
        )

    def on_update(self, delta_time):
        if self.player_list:
            self.player_list.update()

        if self.player and self.player.is_shooting:
            bullet = self.player.weapon.fire(self.player.position, self.player.angle)
            if bullet and self.bullet_list is not None:
                self.bullet_list.append(bullet)

        if self.bullet_list:
            self.bullet_list.update(delta_time)


    def on_key_press(self, symbol, modifiers):
        if self.player:
            if symbol == arcade.key.UP or symbol == arcade.key.W:
                self.player.up_pressed = True
            elif symbol == arcade.key.DOWN or symbol == arcade.key.S:
                self.player.down_pressed = True

            if symbol == arcade.key.LEFT or symbol == arcade.key.A:
                self.player.left_pressed = True
            elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
                self.player.right_pressed = True

            if symbol == arcade.key.SPACE:
                self.player.is_shooting = True

    def on_key_release(self, symbol, modifiers):
        if self.player:
            if symbol == arcade.key.UP or symbol == arcade.key.W:
                self.player.up_pressed = False
            elif symbol == arcade.key.DOWN or symbol == arcade.key.S:
                self.player.down_pressed = False

            if symbol == arcade.key.LEFT or symbol == arcade.key.A:
                self.player.left_pressed = False
            elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
                self.player.right_pressed = False

            if symbol == arcade.key.SPACE:
                self.player.is_shooting = False
