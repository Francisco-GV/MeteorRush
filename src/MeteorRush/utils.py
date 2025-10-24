import arcade

from MeteorRush import constants


def scale_and_center_background(image_path: str) -> arcade.Sprite:
    texture = arcade.load_texture(image_path)

    scale_x = constants.SCREEN_WIDTH / texture.width
    scale_y = constants.SCREEN_HEIGHT / texture.height

    scale = max(scale_x, scale_y)

    background_sprite = arcade.Sprite(texture, scale=scale)
    background_sprite.center_x = constants.SCREEN_WIDTH / 2
    background_sprite.center_y = constants.SCREEN_HEIGHT / 2

    return background_sprite