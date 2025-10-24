import arcade


def load_textures_from_spritesheet(
    file_name: str,
    sprite_size: tuple[int, int],
    columns: int,
    count: int,
    start_index: int = 0,
) -> list[arcade.Texture]:
    spritesheet = arcade.load_spritesheet(file_name)

    texture_grid = spritesheet.get_texture_grid(
        size=sprite_size,
        columns=columns,
        count=count,
    )

    texture_grid = texture_grid[start_index:]

    return texture_grid


def load_textures_from_directory(directory_path: str) -> list[arcade.Texture]:
    from pathlib import Path

    directory = Path(directory_path)

    frame_files = sorted(directory.glob("*.png"))

    texture_list = [arcade.load_texture(file) for file in frame_files]

    return texture_list


def load_textures_from_gif(file_path: str) -> list[arcade.Texture]:
    from PIL import Image, ImageSequence

    texture_list = []
    gif = Image.open(file_path)
    for frame in ImageSequence.Iterator(gif):
        image = frame.copy().convert("RGBA")
        texture = arcade.Texture(image)
        texture_list.append(texture)

    return texture_list
