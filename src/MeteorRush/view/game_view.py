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

        self.up_pressed = False
        self.down_pressed = False

        self.left_pressed = False
        self.right_pressed = False

    def setup(self):
        self.player = Player()
        self.player_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.player_list.append(self.player)

    def on_show_view(self):
        arcade.set_background_color(arcade.color.AMAZON)
        self.setup()

    def on_draw(self):
        self.clear()

        if self.bullet_list:
            self.bullet_list.draw()

        if self.player_list:
            self.player_list.draw()

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
