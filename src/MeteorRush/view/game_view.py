import arcade

from MeteorRush import constants


class GameView(arcade.View):

    def __init__(self):
        super().__init__()
        self.player_sprite = None
        self.player_list = None

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    def setup(self):
        self.player_list = arcade.SpriteList()
        image_source = "assets/images/player/player_ship.png"
        self.player_sprite = arcade.Sprite(image_source, constants.PLAYER_SCALING)
        self.player_sprite.center_x = self.window.width / 2
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

    def on_show_view(self):
        arcade.set_background_color(arcade.color.AMAZON)
        self.setup()

    def on_draw(self):
        self.clear()
        if self.player_list:
            self.player_list.draw()

    def on_update(self, delta_time):
        if self.player_sprite and self.player_list:
            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0

            if self.up_pressed and not self.down_pressed:
                self.player_sprite.change_y = constants.PLAYER_MOVEMENT_SPEED
            elif self.down_pressed and not self.up_pressed:
                self.player_sprite.change_y = -constants.PLAYER_MOVEMENT_SPEED

            if self.left_pressed and not self.right_pressed:
                self.player_sprite.change_x = -constants.PLAYER_MOVEMENT_SPEED
            elif self.right_pressed and not self.left_pressed:
                self.player_sprite.change_x = constants.PLAYER_MOVEMENT_SPEED

            self.player_list.update()

            if self.player_sprite.left < 0:
                self.player_sprite.left = 0
            elif self.player_sprite.right > self.window.width:
                self.player_sprite.right = self.window.width

            if self.player_sprite.bottom < 0:
                self.player_sprite.bottom = 0
            elif self.player_sprite.top > self.window.height:
                self.player_sprite.top = self.window.height

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.UP or symbol == arcade.key.W:
            self.up_pressed = True
        elif symbol == arcade.key.DOWN or symbol == arcade.key.S:
            self.down_pressed = True
        elif symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.left_pressed = True
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.right_pressed = True

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.UP or symbol == arcade.key.W:
            self.up_pressed = False
        elif symbol == arcade.key.DOWN or symbol == arcade.key.S:
            self.down_pressed = False
        elif symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.left_pressed = False
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.right_pressed = False
