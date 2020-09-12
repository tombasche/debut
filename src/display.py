from curses import A_BOLD, A_UNDERLINE, COLOR_RED, COLOR_BLACK, init_pair, color_pair, COLOR_WHITE, COLOR_BLUE
from dataclasses import dataclass
from functools import reduce, partial
from time import sleep
from typing import List


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

    def move_cursor(self):
        self.x += 1

    def set_writing_coords(self):
        self.x += self.x_offset
        self.y += self.y_offset

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

    delay_between_letters = 0.02

    @classmethod
    def display(
        cls,
        coords: List[int],
        text: str,
        screen,
        format_options: List[str] = None,
        highlight_color='black',
        text_color='white',
        animate=True
    ):
        _, max_width = screen.getmaxyx()
        cls.check_if_valid_options(format_options)
        color_pair_choice = get_or_set_color_pair(cls.colors[text_color], cls.colors[highlight_color])

        display_string = partial(
            cls._display_string,
            color_choice=color_pair_choice,
            format_options=format_options,
            screen=screen
        )

        if animate:
            w = AnimatedWriter(coords[1], coords[0], 0, 0, max_width)
            for word in text.split(" "):

                if w.word_will_overflow(len(word)):
                    w.new_line(coords[1])

                for character in word:
                    w.set_writing_coords()
                    
                    if w.at_edge_of_screen:
                        w.new_line(coords[1])

                    display_string(coords=[w.y, w.x], text=character)
                    sleep(cls.delay_between_letters)
                    screen.refresh()
                    w.move_cursor()

                w.move_cursor()
                screen.refresh()
        else:
            display_string(coords=[coords[0], coords[1]], text=text)
        screen.refresh()

    @classmethod
    def _display_string(cls, screen=None, coords=None, text=None, color_choice=None, format_options=None):
        return screen.addstr(coords[0], coords[1], text, cls.combine_options(color_pair(color_choice), format_options))

    @classmethod
    def combine_options(cls, color_pair, format_options: List[str]):
        if not format_options:
            return 0
        if len(format_options) > 1:
            options = reduce(lambda x, y: cls.formatting[x] | cls.formatting[y], format_options)
            return options | color_pair
        return cls.formatting[format_options[0]]

    @classmethod
    def check_if_valid_options(cls, format_options: List[str]):
        if not format_options:
            return
        for option in format_options:
            if option not in cls.formatting:
                raise UnknownFormatOption(option)


def at_edge_of_screen(x: int, max_width: int) -> bool:
    return x >= max_width


def get_or_set_color_pair(text_color: int, highlight_color: int):
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


COLOR_PAIR_CACHE = {}


class UnknownFormatOption(Exception):
    ...


class TooManyColorsSpecified(Exception):
    ...
