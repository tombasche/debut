from time import sleep

from src.display import DisplayString


class Slide:

    def __init__(self, heading: str, text: str):
        self._heading = heading
        self._text = text

    def display(self, screen=None):
        self._display_heading(screen)
        DisplayString.display([3, 5], self._text, screen, text_color='red')
        screen.refresh()

    def _display_heading(self, screen):
        DisplayString.display([0, 5], self._heading, screen, highlight_color='blue', format_options=['bold', 'underline'])
        DisplayString.display([1, 5], "=" * 30, screen, format_options=['bold', 'underline'], animate=False)
        sleep(0.1)
