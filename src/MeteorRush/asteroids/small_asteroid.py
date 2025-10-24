import random
from MeteorRush.asteroids.asteroid import Asteroid
from MeteorRush import constants


class SmallAsteroid(Asteroid):

    IMAGE_PATHS = (
        "assets/images/asteroids/meteorBrown_small1.png",
        "assets/images/asteroids/meteorBrown_small2.png",
    )

    def __init__(self):
        IMAGE_PATH = random.choice(self.IMAGE_PATHS)

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
            image_path=IMAGE_PATH,
            scale=constants.ASTEROID_SML_SCALING,
        )
