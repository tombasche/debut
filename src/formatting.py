from curses import A_BOLD, A_UNDERLINE, A_STANDOUT
from functools import reduce
from typing import List, Dict

from src.colour import COLOURS


class Formatter:

    DECORATION: Dict[str, int] = {
        'bold': A_BOLD,
        'underline': A_UNDERLINE,
        'highlighted': A_STANDOUT,
    }

    FORMATTING: Dict[str, int] = {
        **COLOURS,
        **DECORATION
    }

    def __init__(self, colour_pair: int, format_options: List[str]):
        self._colour_pair = colour_pair
        self._format_options = format_options

        self._check_if_valid_options()

    def combine_options(self):
        if not self._format_options:
            return self._colour_pair
        if len(self._format_options) > 1:
            format_options = [self.FORMATTING[i] for i in self._format_options]
            options = reduce(lambda x, y: x | y, format_options)
            return options | self._colour_pair
        return self.FORMATTING[self._format_options[0]]

    def _check_if_valid_options(self):
        if not self._format_options:
            return
        for option in self._format_options:
            if option not in self.FORMATTING:
                raise UnknownFormatOption(option)


class UnknownFormatOption(Exception):
    ...


