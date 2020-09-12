from curses import A_BOLD, A_UNDERLINE, COLOR_RED, COLOR_BLACK, init_pair, color_pair, COLOR_WHITE, COLOR_BLUE
from dataclasses import dataclass
from functools import reduce, partial
from time import sleep
from typing import List, Dict, Tuple, Optional

from src.interaction import InputListener


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


class DisplayText:

    colors = {
        'red': COLOR_RED,
        'black': COLOR_BLACK,
        'white': COLOR_WHITE,
        'blue': COLOR_BLUE,
    }

    decoration = {
        'bold': A_BOLD,
        'underline': A_UNDERLINE
    }

    formatting = {
        **colors,
        **decoration
    }

    tab_size: int = 4

    def __init__(self, screen, coords: List[int], input_listener: Optional[InputListener] = None):
        self._screen = screen
        self._coords = coords

        max_height, max_width = self._screen.getmaxyx()
        self.max_height: int = max_height
        self.max_width: int = max_width

        self._input_listener = input_listener

    def display(
        self,
        text: str,
        format_options: List[str] = None,
        highlight_color='black',
        text_color='white',
        animate=True,
        custom_character_delay: float = None
    ):

        self.check_if_valid_options(format_options)
        color_pair_choice = get_or_set_color_pair(self.colors[text_color], self.colors[highlight_color])

        display_string = partial(
            self._display_string,
            color_choice=color_pair_choice,
            format_options=format_options,
            screen=self._screen
        )

        left_alignment = self._coords[1]
        coords = self._coords

        if animate:
            w = AnimatedWriter(coords[1], coords[0], 0, 0, self.max_width)
            for word in text.split(" "):

                if w.word_will_overflow(len(word)):
                    w.new_line(left_alignment)

                for character in word:
                    w.set_default_writing_coords()

                    if w.at_edge_of_screen:
                        w.new_line(left_alignment)

                    if character == '\n':
                        w.new_line(left_alignment)
                        left_alignment = coords[1] -1

                        if self._input_listener:
                            self._input_listener.wait_for_input()
                    elif character == '\t':
                        left_alignment += self.tab_size

                    else:
                        left_alignment = self._coords[1]

                    display_string(coords=[w.y, w.x], text=character)
                    sleep(custom_character_delay or character_delay(text))
                    self.auto_redraw()
                    w.move_cursor()

                w.move_cursor()
                self.auto_redraw()
        else:
            display_string(coords=[coords[0], coords[1]], text=text)

        self.auto_redraw()

    def auto_redraw(self):
        self._screen.refresh()

    def _display_string(self, screen=None, coords=None, text=None, color_choice=None, format_options=None):
        return screen.addstr(coords[0], coords[1], text, self.combine_options(color_pair(color_choice), format_options))

    def combine_options(self, color_pair, format_options: List[str]):
        if not format_options:
            return color_pair
        if len(format_options) > 1:
            options = reduce(lambda x, y: self.formatting[x] | self.formatting[y], format_options)
            return options | color_pair
        return self.formatting[format_options[0]]

    def check_if_valid_options(self, format_options: List[str]):
        if not format_options:
            return
        for option in format_options:
            if option not in self.formatting:
                raise UnknownFormatOption(option)

    def shift_y_by(self, shift: int):
        self._coords[0] += shift


def character_delay(text: str) -> float:
    return min(3 / len(text), 0.03)


def get_or_set_color_pair(text_color: int, highlight_color: int) -> int:
    color_pair_values = list(COLOR_PAIR_CACHE.values())
    if color_pair_values:
        last_pair = max(color_pair_values)
    else:
        last_pair = 0
    if last_pair == 256:
        raise TooManyColorsSpecified
    if (text_color, highlight_color) in COLOR_PAIR_CACHE:
        return COLOR_PAIR_CACHE[(text_color, highlight_color)]

    next_available_pair = last_pair + 1
    COLOR_PAIR_CACHE[(text_color, highlight_color)] = next_available_pair
    init_pair(next_available_pair, text_color, highlight_color)
    return next_available_pair


COLOR_PAIR_CACHE: Dict[Tuple[int, int], int] = {}


class UnknownFormatOption(Exception):
    ...


class TooManyColorsSpecified(Exception):
    ...
