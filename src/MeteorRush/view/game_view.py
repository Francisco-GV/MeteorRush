import math
import random

import arcade

from MeteorRush import constants
from MeteorRush.asteroids.asteroid import Asteroid
from MeteorRush.effects.explosion import Explosion
from MeteorRush.sprites.player import Player
from MeteorRush.util.textures import load_textures_from_spritesheet
from MeteorRush.utils import scale_and_center_background

from MeteorRush.components.bar import Bar

class GameView(arcade.View):

    def __init__(self):
        super().__init__()
        self.player = None
        self.player_list = None
        self.bullet_list = None
        self.asteroid_list = None

        self.explosion_list = None
        self.background_list = None
        self.ammo_texture = None
        self.background = None

        self.player_health_bar = None

        self.up_pressed = False
        self.down_pressed = False

        self.left_pressed = False
        self.right_pressed = False

        self.asteroid_hit_textures = []
        self.asteroid_explosion_textures = []
        self.player_hit_textures = []
        self.player_explosion_textures = []

        self.asteroid_hit_sound = None
        self.asteroid_explosion_sound = None
        self.player_hit_sound = None
        self.player_explosion_sound = None

        self.asteroid_spawn_timer = 0.0

        self.text_fps = None
        self.first_update = True

    def setup(self):
        self.player = Player()
        self.player_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()
        self.explosion_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()

        health_bar_height = 25
        health_bar_width = 20
        health_bar_margin = 20
        self.player_health_bar = Bar(
            self.player.max_health,
            x=health_bar_margin,
            y=self.window.height - health_bar_height - health_bar_margin,
            width=health_bar_width,
            height=health_bar_height,
        )

        self.player_list.append(self.player)

        for _ in range(constants.ASTEROID_INITIAL_COUNT):
            self._spawn_asteroid()

        if self.player:
            self.ammo_texture = arcade.load_texture(
                self.player.weapon.bullet_texture_path
            )

        background_sprite = scale_and_center_background(
            "assets/images/backgrounds/space_background.png"
        )
        self.background_list.append(background_sprite)

        self.asteroid_hit_textures = load_textures_from_spritesheet(
            "assets/spritesheets/Effect_Impact_1_305x383.png",
            sprite_size=(305, 383),
            columns=9,
            count=60,
        )
        self.asteroid_explosion_textures = load_textures_from_spritesheet(
            "assets/spritesheets/Effect_Explosion_1_517x517.png",
            sprite_size=(517, 517),
            columns=9,
            count=60,
        )
        self.player_hit_textures = load_textures_from_spritesheet(
            "assets/spritesheets/Effect_PuffAndStars_1_108x116.png",
            sprite_size=(108, 116),
            columns=10,
            count=80,
        )

        self.player_explosion_textures = load_textures_from_spritesheet(
            "assets/spritesheets/Effect_Explosion2_1_355x365.png",
            sprite_size=(355, 365),
            columns=9,
            count=60,
        )

        self.asteroid_hit_sound = arcade.load_sound("assets/sounds/explosions/lowFrequency_explosion_001.wav")
        self.asteroid_explosion_sound = arcade.load_sound("assets/sounds/explosions/explosionCrunch_004.wav")
        self.player_hit_sound = arcade.load_sound("assets/sounds/explosions/explosionCrunch_000.wav")
        self.player_explosion_sound = arcade.load_sound("assets/sounds/explosions/explosionCrunch_001.wav")

        self.text_fps = arcade.Text(
            "",
            x=constants.SCREEN_WIDTH - 50,
            y=10,
            color=arcade.color.WHITE,
            font_size=10,
        )

    def on_show_view(self):
        arcade.set_background_color(arcade.color.AMAZON)
        self.setup()

    def on_draw(self):
        self.clear()

        if self.background_list:
            self.background_list.draw()

        if self.asteroid_list:
            self.asteroid_list.draw()

        if self.bullet_list:
            self.bullet_list.draw()

        if self.player_list:
            self.player_list.draw()

        if self.explosion_list:
            self.explosion_list.draw()

        if self.player and self.ammo_texture:
            ammo_start_x = self.ammo_texture.width + 15
            ammo_start_y = self.ammo_texture.height + 5
            ammo_spacing = 15
            ammo_scale = 0.8

            scaled_width = self.ammo_texture.width * ammo_scale
            scaled_height = self.ammo_texture.height * ammo_scale

            weapon = self.player.weapon

            i = 0
            while i < weapon.magazine_size:
                center_x = ammo_start_x + i * ammo_spacing
                center_y = ammo_start_y
                bottom_left_x = center_x - (scaled_width / 2)
                bottom_left_y = center_y - (scaled_height / 2)

                arcade.draw_texture_rect(
                    texture=self.ammo_texture,
                    rect=arcade.XYWH(
                        x=bottom_left_x,
                        y=bottom_left_y,
                        width=scaled_width,
                        height=scaled_height,
                    ),
                    alpha=255 if i < weapon.current_ammo else 100
                )

                i += 1

        if self.player_health_bar and self.player:
            self.player_health_bar.draw(self.player.current_health)

        if self.text_fps:
            fps = arcade.get_fps()
            self.text_fps.text = f"FPS: {fps:.0f}"
            self.text_fps.draw()

    def on_update(self, delta_time):
        if self.first_update:
            self.first_update = False
            return

        if delta_time > 0.1:
            delta_time = 0.1

        if self.player_list:
            self.player_list.update()

        if self.asteroid_list:
            self.asteroid_list.update()

            self.asteroid_spawn_timer += delta_time
            if self.asteroid_spawn_timer >= constants.ASTEROID_SPAWN_INTERVAL:
                self._spawn_asteroid()
                self.asteroid_spawn_timer = 0.0

        if self.player and self.player.is_alive and self.player.is_shooting:
            bullet = self.player.weapon.fire(self.player.position, self.player.angle)
            if bullet and self.bullet_list is not None:
                self.bullet_list.append(bullet)

        if self.bullet_list:
            self.bullet_list.update(delta_time)

        if self.explosion_list:
            self.explosion_list.update(delta_time)

        self._handle_collisions()

    def _spawn_asteroid(self):
        image_path = "assets/images/asteroids/asteroid.png"
        asteroid = Asteroid(image_path, constants.ASTEROID_SCALING)

        side = random.choice(["top", "bottom", "left", "right"])

        match (side):
            case "top":
                asteroid.center_x = random.uniform(0, constants.SCREEN_WIDTH)
                asteroid.bottom = constants.SCREEN_HEIGHT
            case "bottom":
                asteroid.center_x = random.uniform(0, constants.SCREEN_WIDTH)
                asteroid.top = 0
            case "left":
                asteroid.center_y = random.uniform(0, constants.SCREEN_HEIGHT)
                asteroid.right = 0
            case "right":
                asteroid.center_y = random.uniform(0, constants.SCREEN_HEIGHT)
                asteroid.left = constants.SCREEN_WIDTH

        if self.asteroid_list is not None:
            self.asteroid_list.append(asteroid)

    def _handle_collisions(self):
        if self.asteroid_list and self.bullet_list:
            for bullet in self.bullet_list:
                hit_list = arcade.check_for_collision_with_list(
                    sprite=bullet, sprite_list=self.asteroid_list
                )

                if hit_list:
                    bullet.remove_from_sprite_lists()

                    for asteroid in hit_list:
                        explosion = Explosion(
                            self.asteroid_hit_textures,
                            asteroid.center_x,
                            asteroid.center_y,
                            sound=self.asteroid_hit_sound,
                            sound_conf=dict(volume=0.25),
                        )
                        self.explosion_list.append(explosion)

                        asteroid.current_health -= bullet.damage
                        if asteroid.current_health <= 0:
                            explosion = Explosion(
                                self.asteroid_explosion_textures,
                                asteroid.center_x,
                                asteroid.center_y,
                                sound=self.asteroid_explosion_sound,
                            )
                            self.explosion_list.append(explosion)

                            asteroid.remove_from_sprite_lists()

        if self.player and self.player.is_alive and self.asteroid_list:
            hit_list = arcade.check_for_collision_with_list(
                sprite=self.player, sprite_list=self.asteroid_list
            )

            if hit_list:
                for asteroid in hit_list:
                    self.player.current_health -= asteroid.collision_damage
                    explosion = Explosion(
                        self.player_hit_textures,
                        asteroid.center_x,
                        asteroid.center_y,
                        sound=self.player_hit_sound,
                    )
                    self.explosion_list.append(explosion)

                    asteroid.remove_from_sprite_lists()

                    if self.player.current_health <= 0:
                        explosion = Explosion(
                            self.player_explosion_textures,
                            self.player.center_x,
                            self.player.center_y,
                            sound=self.player_explosion_sound,
                        )
                        self.explosion_list.append(explosion)

                        self.player.remove_from_sprite_lists()
                        self.player.is_alive = False

    def on_key_press(self, symbol, modifiers):
        if self.player and self.player.is_alive:
            if symbol == arcade.key.UP or symbol == arcade.key.W:
                self.player.up_pressed = True
            elif symbol == arcade.key.DOWN or symbol == arcade.key.S:
                self.player.down_pressed = True

            if symbol == arcade.key.LEFT or symbol == arcade.key.A:
                self.player.left_pressed = True
            elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
                self.player.right_pressed = True

            if symbol == arcade.key.SPACE:
                self.player.is_shooting = True

    def on_key_release(self, symbol, modifiers):
        if self.player:
            if symbol == arcade.key.UP or symbol == arcade.key.W:
                self.player.up_pressed = False
            elif symbol == arcade.key.DOWN or symbol == arcade.key.S:
                self.player.down_pressed = False

            if symbol == arcade.key.LEFT or symbol == arcade.key.A:
                self.player.left_pressed = False
            elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
                self.player.right_pressed = False

            if symbol == arcade.key.SPACE:
                self.player.is_shooting = False
