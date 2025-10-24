import random
from MeteorRush.asteroids.asteroid import Asteroid
from MeteorRush import constants


class MediumAsteroid(Asteroid):

    IMAGE_PATHS = (
        "assets/images/asteroids/meteorBrown_med1.png",
        "assets/images/asteroids/meteorBrown_med3.png",
    )

    def __init__(self):
        IMAGE_PATH = random.choice(self.IMAGE_PATHS)

        super().__init__(
            max_health=constants.ASTEROID_MID_MAX_HEALTH,
            collision_damage=constants.ASTEROID_MID_COLLISION_DAMAGE,
            speed_range=(
                constants.ASTEROID_MID_SPEED_MIN,
                constants.ASTEROID_MID_SPEED_MAX,
            ),
            rotation_speed_range=(
                constants.ASTEROID_MID_ROTATION_SPEED_MIN,
                constants.ASTEROID_MID_ROTATION_SPEED_MAX,
            ),
            image_path=IMAGE_PATH,
            scale=constants.ASTEROID_MID_SCALING,
        )
