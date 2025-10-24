from MeteorRush.asteroids.asteroid import Asteroid
from MeteorRush import constants


class TinyAsteroid(Asteroid):

    IMAGE_PATH = "assets/images/asteroids/meteorBrown_tiny1.png"

    def __init__(self):
        super().__init__(
            max_health=constants.ASTEROID_TIN_MAX_HEALTH,
            collision_damage=constants.ASTEROID_TIN_COLLISION_DAMAGE,
            speed_range=(
                constants.ASTEROID_TIN_SPEED_MIN,
                constants.ASTEROID_TIN_SPEED_MAX,
            ),
            rotation_speed_range=(
                constants.ASTEROID_TIN_ROTATION_SPEED_MIN,
                constants.ASTEROID_TIN_ROTATION_SPEED_MAX,
            ),
            image_path=self.IMAGE_PATH,
            scale=constants.ASTEROID_TIN_SCALING,
        )
