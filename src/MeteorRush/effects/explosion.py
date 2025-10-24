import arcade


class Explosion(arcade.Sprite):
    def __init__(self, texture_list: list, center_x: float, center_y: float):
        super().__init__()

        self.center_x = center_x
        self.center_y = center_y

        self.textures = texture_list
        self.cur_texture_index = 0
        self.texture = self.textures[self.cur_texture_index]

    def update(self, _delta_time):
        self.cur_texture_index += 1

        if self.cur_texture_index >= len(self.textures):
            self.remove_from_sprite_lists()
        else:
            self.texture = self.textures[self.cur_texture_index]
