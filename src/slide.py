from time import sleep

from src.display import DisplayText
from src.text import Text


class Slide:

    def __init__(self, heading: str, text: Text, advance_new_lines_after_input=True):
        self._heading = heading
        self._text = text
        self.advance_new_lines_after_input = advance_new_lines_after_input

    def display(self, screen=None):
        self._display_heading(screen)
        DisplayText.display([3, 5], self._text.render(), screen, text_color='red')

    def _display_heading(self, screen):
        DisplayText.display([0, 5], self._heading, screen, highlight_color='blue', format_options=['bold', 'underline'])
        DisplayText.display([1, 5], "=" * len(self._heading), screen, format_options=['bold', 'underline'], animate=False)
        sleep(0.1)
