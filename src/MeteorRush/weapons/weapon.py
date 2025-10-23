import abc
from collections import deque
from typing import Optional

import arcade


class Weapon(abc.ABC):
    def __init__(
        self,
        damage: int,
        fire_rate: float,
        magazine_size: int,
        reload_speed: float,
        bullet_texture_path: str,
    ):
        self.damage = damage
        self.fire_rate = fire_rate
        self.magazine_size = magazine_size
        self.reload_speed = reload_speed
        self.bullet_texture_path = bullet_texture_path

        self.current_ammo = magazine_size
        self.cooldown_timer = 0.0
        self.reload_queue = deque()

    @abc.abstractmethod
    def fire(
        self, position: tuple[float, float], angle: float
    ) -> Optional[arcade.Sprite]:
        pass

    def update(self, delta_time: float):
        if self.cooldown_timer > 0:
            self.cooldown_timer -= delta_time
            if self.cooldown_timer < 0:
                self.cooldown_timer = 0

        if self.reload_queue:
            self.reload_queue[0] -= delta_time

            if self.reload_queue[0] <= 0:
                self.reload_queue.popleft()
                self.current_ammo += 1
