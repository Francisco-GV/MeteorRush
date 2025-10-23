import arcade

from MeteorRush import constants


class LaserBullet(arcade.Sprite):

    def __init__(self):
        self.scaling = 0.8
        self.speed = 7

        super().__init__("assets/images/lasers/laser_green.png", scale=self.scaling)

    def update(self, _):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if (
            self.top < 0
            or self.bottom > constants.SCREEN_HEIGHT
            or self.right < 0
            or self.left > constants.SCREEN_WIDTH
        ):
            self.remove_from_sprite_lists()
