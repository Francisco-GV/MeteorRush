from MeteorRush.asteroids.asteroid import Asteroid
from MeteorRush import constants


class SmallAsteroid(Asteroid):

    IMAGE_PATH = "assets/images/asteroids/meteorBrown_small1.png"

    def __init__(self):
        super().__init__(
            max_health=constants.ASTEROID_SML_MAX_HEALTH,
            collision_damage=constants.ASTEROID_SML_COLLISION_DAMAGE,
            speed_range=(
                constants.ASTEROID_SML_SPEED_MIN,
                constants.ASTEROID_SML_SPEED_MAX,
            ),
            rotation_speed_range=(
                constants.ASTEROID_SML_ROTATION_SPEED_MIN,
                constants.ASTEROID_SML_ROTATION_SPEED_MAX,
            ),
            image_path=self.IMAGE_PATH,
            scale=constants.ASTEROID_SML_SCALING,
        )
