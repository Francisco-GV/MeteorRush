from MeteorRush.asteroids.asteroid import Asteroid
from MeteorRush import constants


class LargeAsteroid(Asteroid):

    IMAGE_PATH = "assets/images/asteroids/meteorBrown_big1.png"

    def __init__(self):
        super().__init__(
            max_health=constants.ASTEROID_BIG_MAX_HEALTH,
            collision_damage=constants.ASTEROID_BIG_COLLISION_DAMAGE,
            speed_range=(
                constants.ASTEROID_BIG_SPEED_MIN,
                constants.ASTEROID_BIG_SPEED_MAX,
            ),
            rotation_speed_range=(
                constants.ASTEROID_BIG_ROTATION_SPEED_MIN,
                constants.ASTEROID_BIG_ROTATION_SPEED_MAX,
            ),
            image_path=self.IMAGE_PATH,
            scale=constants.ASTEROID_BIG_SCALING,
        )
