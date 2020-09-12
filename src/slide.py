
from src.display import DisplayText
from src.interaction import InputListener
from src.text import Text


class Slide:

    def __init__(self, heading: str, text: Text, advance_on_input=True):
        self._heading = heading
        self._text = text
        self.advance_on_input = advance_on_input

    def display(self, screen):

        input_listener = None
        if self.advance_on_input:
            input_listener = InputListener(screen)
        self._display_heading(screen, input_listener)

        slide_body = DisplayText(screen=screen, coords=[3, 5], input_listener=input_listener)
        slide_body.display(
            text=self._text.render(),
            text_color='red'
        )

    def _display_heading(self, screen, input_listener):

        heading_text = DisplayText(screen=screen, coords=[0, 5])
        heading_text.display(text=self._heading, format_options=['bold', 'underline'], highlight_color='blue')

        underline = DisplayText(screen=screen, coords=[1, 5])
        underline.display(text="=" * len(self._heading), animate=False)

        if input_listener:
            input_listener.wait_for_input()

