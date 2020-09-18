from dataclasses import dataclass


@dataclass
class AnimatedWriter:
    x: int
    y: int

    x_offset: int
    y_offset: int

    max_width: int

    def new_line(self, initial_x: int):
        self.x = initial_x
        self.y += 1

    def move_cursor(self, amount: int = 1):
        self.x += amount

    def set_default_writing_coords(self):
        self.x += self.x_offset
        self.y += self.y_offset

    def set_custom_writing_coords(self, x: int, y: int):
        self.x += x
        self.y += y

    @property
    def at_edge_of_screen(self) -> bool:
        return self.x >= self.max_width

    def word_will_overflow(self, word_length: int) -> bool:
        return word_length + self.x + self.x_offset >= self.max_width
