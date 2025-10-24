import arcade


class Explosion(arcade.Sprite):
    def __init__(
        self,
        texture_list: list,
        center_x: float,
        center_y: float,
        sound: arcade.Sound = None,
        sound_conf: dict = None,
    ):
        super().__init__()

        self.center_x = center_x
        self.center_y = center_y

        self.textures = texture_list
        self.cur_texture_index = 0
        self.texture = self.textures[self.cur_texture_index]

        self.sound = sound
        self.sound_conf = sound_conf

    def update(self, _delta_time):
        if self.cur_texture_index == 0 and self.sound:
            sound_conf = self.sound_conf if self.sound_conf else {}
            arcade.play_sound(self.sound, **sound_conf)

        self.cur_texture_index += 1

        if self.cur_texture_index >= len(self.textures):
            self.remove_from_sprite_lists()
        else:
            self.texture = self.textures[self.cur_texture_index]
