import math
import random

import arcade

from MeteorRush import constants


class Asteroid(arcade.Sprite):
    def __init__(
        self,
        max_health: int,
        collision_damage: int,
        speed_range: tuple[int, int],
        rotation_speed_range: tuple[int, int],
        image_path: str,
        scale: float,
    ):
        super().__init__(image_path, scale=scale)

        self.max_health = max_health
        self.current_health = self.max_health
        self.collision_damage = collision_damage

        self.speed = random.uniform(speed_range[0], speed_range[1])
        self.change_angle = random.uniform(
            rotation_speed_range[0], rotation_speed_range[1]
        )

        direction_rad = math.radians(random.uniform(0, 360))
        self.change_x = math.cos(direction_rad) * self.speed
        self.change_y = math.sin(direction_rad) * self.speed

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
