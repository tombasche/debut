from curses import A_BOLD, A_UNDERLINE, COLOR_RED, COLOR_BLACK, init_pair, color_pair, COLOR_WHITE, COLOR_BLUE
from functools import reduce
from time import sleep
from typing import List


class DisplayString:

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
        max_height, max_width = screen.getmaxyx()
        cls.check_if_valid_options(format_options)
        color_pair_choice = get_or_set_color_pair(cls.colors[text_color], cls.colors[highlight_color])

        if animate:
            x_offset = 0
            y_offset = 0
            for i, character in enumerate(text):
                y = coords[0] + y_offset
                x = coords[1] + x_offset
                if x >= max_width:
                    x_offset = 0
                    y_offset += 1
                    y = coords[0] + y_offset
                    x = coords[1] + x_offset
                screen.addstr(y, x, character, cls.combine_options(color_pair(color_pair_choice), format_options))
                sleep(cls.delay_between_letters)
                screen.refresh()
                x_offset += 1

        else:
            screen.addstr(coords[0], coords[1], text,
                          cls.combine_options(color_pair(color_pair_choice), format_options))


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