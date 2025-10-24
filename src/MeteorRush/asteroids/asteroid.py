import math
import random

import arcade

from MeteorRush import constants


class Asteroid(arcade.Sprite):

    def __init__(self, image_path: str, scale: float):
        super().__init__(image_path, scale)

        self.max_health = 3
        self.current_health = self.max_health
        self.collision_damage = 3

        self.speed = random.uniform(
            constants.ASTEROID_MIN_SPEED, constants.ASTEROID_MAX_SPEED
        )

        direction_rad = math.radians(random.uniform(0, 360))
        self.change_x = math.cos(direction_rad) * self.speed
        self.change_y = math.sin(direction_rad) * self.speed

        self.change_angle = random.uniform(
            constants.ASTEROID_MIN_ROTATION_SPEED, constants.ASTEROID_MAX_ROTATION_SPEED
        )

    def update(self, delta_time):
        super().update(delta_time)

        if self.left > constants.SCREEN_WIDTH:
            self.right = 0
        elif self.right < 0:
            self.left = constants.SCREEN_WIDTH

        if self.bottom > constants.SCREEN_HEIGHT:
            self.top = 0
        elif self.top < 0:
            self.bottom = constants.SCREEN_HEIGHT
