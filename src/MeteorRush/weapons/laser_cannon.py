import math
from pathlib import Path

import arcade

from MeteorRush.sprites.laser_bullet import LaserBullet
from MeteorRush.weapons.weapon import Weapon


class LaserCannon(Weapon):
    def __init__(self):
        super().__init__(
            damage=1,
            fire_rate=0.5,
            magazine_size=10,
            reload_speed=1.0,
            bullet_texture_path=LaserBullet.TEXTURE_PATH,
        )
        self.laser_sound = arcade.load_sound(Path(r"assets/sounds/lasers/laser.wav"))

    def fire(self, position: tuple[float, float], angle: float):
        if self.cooldown_timer <= 0 and self.current_ammo > 0:
            self.current_ammo -= 1
            self.cooldown_timer = self.fire_rate

            self.reload_queue.append(self.reload_speed)

            if self.laser_sound:
                arcade.play_sound(self.laser_sound)

            bullet = LaserBullet()
            bullet.center_x = position[0]
            bullet.center_y = position[1]
            bullet.angle = angle

            angle_rad = math.radians(angle + 90)
            bullet.change_x = -math.cos(angle_rad) * bullet.speed
            bullet.change_y = math.sin(angle_rad) * bullet.speed

            return bullet
