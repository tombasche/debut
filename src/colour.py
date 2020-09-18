from curses import (
    init_pair,
    color_pair,
    COLOR_RED,
    COLOR_BLUE,
    COLOR_WHITE,
    COLOR_BLACK,
    COLOR_YELLOW
)
from dataclasses import dataclass
from typing import Dict


@dataclass
class ColourPair:
    text: int
    highlight: int

    def __hash__(self):
        return hash((self.text, self.highlight))


class ColourPairs:

    MAX_COLOURS = 256

    def __init__(self):
        self.cache: Dict[ColourPair, int] = {}

    def get(self, colour_pair: ColourPair) -> int:
        most_recent_pair = self._most_recent_pair

        self._check_if_max_colours_reached(most_recent_pair)

        if colour_pair in self.cache:
            return self.cache[colour_pair]

        next_available_slot = self._register_new_pair(colour_pair, most_recent_pair)
        return self._retrieve_color_pair(next_available_slot)

    def _retrieve_color_pair(self, slot: int):
        return color_pair(slot)

    @property
    def _most_recent_pair(self) -> int:
        colour_pair_values = list(self.cache.values())
        if colour_pair_values:
            most_recent_pair = max(colour_pair_values)
        else:
            most_recent_pair = 0
        return most_recent_pair

    def _register_new_pair(self, colour_pair: ColourPair, most_recent_pair: int) -> int:
        next_available_slot = most_recent_pair + 1
        self.cache[colour_pair] = next_available_slot
        self._init_colour_pair(colour_pair, next_available_slot)
        return next_available_slot

    def _init_colour_pair(self, colour_pair: ColourPair, next_available_slot: int):
        init_pair(next_available_slot, colour_pair.text, colour_pair.highlight)

    def _check_if_max_colours_reached(self, latest_pair: int):
        if latest_pair == self.MAX_COLOURS:
            raise TooManyColoursSpecified


class TooManyColoursSpecified(Exception):
    ...


COLOURS = {
    'red': COLOR_RED,
    'black': COLOR_BLACK,
    'white': COLOR_WHITE,
    'blue': COLOR_BLUE,
    'yellow': COLOR_YELLOW
}
