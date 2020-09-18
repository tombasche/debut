from functools import partial
from time import sleep
from typing import List, Optional, Callable

from src.animate import AnimatedWriter
from src.colour import ColourPairs, COLOURS, ColourPair
from src.formatting import Formatter
from src.interaction import InputListener


cp = ColourPairs()


class DisplayText:

    tab_size: int = 4

    def __init__(self, screen, coords: List[int], input_listener: Optional[InputListener] = None):
        self._screen = screen
        self._coords = coords

        max_height, max_width = self._screen.getmaxyx()
        self.max_height: int = max_height
        self.max_width: int = max_width

        self._input_listener = input_listener

        self._left_alignment = self._coords[1]

        self._display_func = None

    def display(
        self,
        text: str,
        format_options: List[str] = None,
        highlight_colour=None,
        text_colour=None,
    ):
        self._instantiate_display_options(text_colour, highlight_colour, format_options)
        self._display(text)
        self.auto_redraw()

    def _display(self, text: str):
        self._display_func(coords=[self._coords[0], self._coords[1]], text=text)

    def _instantiate_display_options(self, text_colour, highlight_colour, format_options):
        highlight_colour = highlight_colour or 'black'
        text_colour = text_colour or 'white'
        display_string_func = self._build_display_function(text_colour, highlight_colour, format_options)
        self._display_func = display_string_func

    def _build_display_function(self, text_colour: str, highlight_colour: str, format_options: List[str]) -> Callable:
        colour_pair = ColourPair(text=COLOURS[text_colour], highlight=COLOURS[highlight_colour])
        colour_pair_choice = cp.get(colour_pair)
        formatter = Formatter(
            colour_pair=colour_pair_choice,
            format_options=format_options
        )
        combined_options = formatter.combine_options()
        display_string = partial(
            self._display_string,
            combined_options=combined_options,
            screen=self._screen
        )
        return display_string

    def auto_redraw(self):
        self._screen.refresh()

    def _display_string(self, screen=None, coords=None, text=None, combined_options=None):
        return screen.addstr(coords[0], coords[1], text, combined_options)

    def shift_y_by(self, shift: int):
        self._coords[0] += shift

    def _advance_on_input(self):
        if self._input_listener:
            self._input_listener.wait_for_input()


class AnimatedText(DisplayText):

    def _display(self, text: str):
        w = AnimatedWriter(self._coords[1], self._coords[0], 0, 0, self.max_width)
        for word in text.split(" "):

            if w.word_will_overflow(len(word)):
                w.new_line(self._left_alignment)

            for character in word:
                w.set_default_writing_coords()

                if w.at_edge_of_screen:
                    w.new_line(self._left_alignment)

                if self._is_newline_character(character):
                    w.new_line(self._left_alignment)
                    self._left_alignment = self._coords[1] - 1

                    self._advance_on_input()

                elif self._is_tab_character(character):
                    self._left_alignment += self.tab_size

                else:
                    self._left_alignment = self._coords[1]

                self._display_func(coords=[w.y, w.x], text=character)
                sleep(self._character_delay(text))
                self.auto_redraw()
                w.move_cursor()

            w.move_cursor()
            self.auto_redraw()

        self.auto_redraw()

    def _character_delay(self, text: str) -> float:
        return min(3 / len(text), 0.03)

    def _is_newline_character(self, character: str) -> bool:
        return character == '\n'

    def _is_tab_character(self, character: str) -> bool:
        return character == '\t'
