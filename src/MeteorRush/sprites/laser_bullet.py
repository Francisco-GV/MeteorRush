import arcade

from MeteorRush import constants


class LaserBullet(arcade.Sprite):

    TEXTURE_PATH = "assets/images/lasers/laser_green.png"

    def __init__(self, damage):
        self.scaling = 0.8
        self.speed = 7
        self.damage = damage

        super().__init__(self.TEXTURE_PATH, scale=self.scaling)

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
