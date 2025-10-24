import arcade


class Bar:
    def __init__(
        self,
        max_value: int,
        x: float,
        y: float,
        height: int,
        width: int = 5,
        spacing: int = 2,
        full_color = arcade.color.GREEN,
        empty_color = (100, 0, 0),
    ):
        self.max_value = max_value
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.spacing = spacing

        self.full_color = full_color
        self.empty_color = empty_color

    def draw(self, current_value: int):
        for i in range(self.max_value):
            bar_x = self.x + i * (self.width + self.spacing)

            color = self.full_color if i < current_value else self.empty_color

            rect = arcade.LBWH(bar_x, self.y, self.width, self.height)
            arcade.draw_rect_filled(
                rect=rect,
                color=color,
            )
