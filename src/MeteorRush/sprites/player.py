import math

import arcade

from MeteorRush import constants
from MeteorRush.weapons.laser_cannon import LaserCannon


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(
            "assets/images/player/player_ship.png",
            scale=constants.PLAYER_SCALING,
        )

        self.center_x = constants.SCREEN_WIDTH / 2
        self.center_y = 50

        self.weapon = LaserCannon()
        self.is_shooting = False

        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False

    def update(self, delta_time = 1 / 60):
        self.weapon.update(delta_time)

        self.change_x = 0
        self.change_y = 0
        self.change_angle = 0

        # Lógica de rotación
        if self.left_pressed and not self.right_pressed:
            self.change_angle = -constants.PLAYER_ROTATION_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.change_angle = constants.PLAYER_ROTATION_SPEED

        # Lógica de movimiento
        if self.up_pressed:
            angle_rad = math.radians(self.angle + 90)
            self.change_x = -math.cos(angle_rad) * constants.PLAYER_MOVEMENT_SPEED * delta_time
            self.change_y = math.sin(angle_rad) * constants.PLAYER_MOVEMENT_SPEED * delta_time
        elif self.down_pressed:
            angle_rad = math.radians(self.angle + 90)
            self.change_x = math.cos(angle_rad) * constants.PLAYER_MOVEMENT_SPEED * delta_time
            self.change_y = -math.sin(angle_rad) * constants.PLAYER_MOVEMENT_SPEED * delta_time

        self.center_x += self.change_x
        self.center_y += self.change_y
        self.angle += self.change_angle

        self._keep_within_bounds()

    def _keep_within_bounds(self):
        if self.center_x < 0:
            self.center_x = 0
        elif self.center_x > constants.SCREEN_WIDTH:
            self.center_x = constants.SCREEN_WIDTH

        if self.center_y < 0:
            self.center_y = 0
        elif self.center_y > constants.SCREEN_HEIGHT:
            self.center_y = constants.SCREEN_HEIGHT
