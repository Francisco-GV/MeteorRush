import random
from MeteorRush.asteroids.asteroid import Asteroid
from MeteorRush import constants


class LargeAsteroid(Asteroid):
    SCORE_VALUE = 10
    TYPE_NAME = "large"

    IMAGE_PATHS = (
        "assets/images/asteroids/meteorBrown_big1.png",
        "assets/images/asteroids/meteorBrown_big2.png",
        "assets/images/asteroids/meteorBrown_big3.png",
        "assets/images/asteroids/meteorBrown_big4.png",
    )

    def __init__(self):
        IMAGE_PATH = random.choice(self.IMAGE_PATHS)

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
            image_path=IMAGE_PATH,
            scale=constants.ASTEROID_BIG_SCALING,
        )
