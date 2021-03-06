from typing import List, Optional

from debut.display import DisplayTextFactory
from debut.interaction import InputListener
from debut.text import Text


class Slide:

    def __init__(
        self,
        heading: str,
        text: Text,
        advance_on_input: bool = True,
        animated_body: bool = True,
        animated_heading: bool = False,
        body_formatting_options: Optional[List[str]] = None,
        body_text_colour: Optional[str] = None,
        body_highlight_colour: Optional[str] = None,
        border: Optional[str] = None
    ):
        self._heading = heading
        self._text = text
        self.advance_on_input = advance_on_input

        self._animated_heading = animated_heading
        self._animated_body = animated_body

        self._body_formatting_options = body_formatting_options
        self._body_text_colour = body_text_colour
        self._body_highlight_colour = body_highlight_colour

        if border and len(border) > 1:
            raise InvalidBorder(f"Border must be a single character, not '{border}'")

        self._border = border

        self.page_number = None

        self.max_height = None
        self.max_width = None

        self._display_factory_method = DisplayTextFactory.create
        self._input_listener_class = InputListener

    def display(self, screen):

        input_listener = None
        if self.advance_on_input:
            input_listener = self._input_listener_class(screen)

        if self._border:
            self._display_border(screen)

        if self.page_number:
            self._show_page_number(screen)

        self._display_heading(screen, input_listener)

        self._display_body(input_listener, screen)

        self._display_nav_indicator(screen)

    def _display_body(self, input_listener, screen):
        slide_body = self._display_factory_method(
            screen=screen, coords=[4, 3],
            input_listener=input_listener,
            animate=self._animated_body
        )
        slide_body.display(text=self._text.render(), format_options=self._body_formatting_options)

    def _display_heading(self, screen, input_listener: InputListener):

        heading_text = self._display_factory_method(screen=screen, coords=[1, 5], animate=self._animated_heading)
        heading_text.display(
            text=self._heading,
            format_options=['bold', 'underline'],
            highlight_colour='blue'
        )

        underline = self._display_factory_method(screen=screen, coords=[2, 5])
        underline.display(text="=" * len(self._heading))

        if input_listener:
            input_listener.wait_for_input()

    def _display_nav_indicator(self, screen):
        nav_indicator = self._display_factory_method(screen=screen, coords=[self.max_height - 1, 1])
        nav_indicator.display(text="<< | >> ", highlight_colour='red', text_colour='white')

    def _display_border(self, screen):
        screen.border(self._border)

    def _show_page_number(self, screen):
        page_number = self._display_factory_method(screen=screen, coords=[self.max_height - 1, self.max_width // 2])
        page_number.display(text=self.page_number)


class TitleSlide:

    def __init__(self, title: str, author: str):
        self._title = title
        self._author = author

    def display(self, screen):
        max_height, max_width = screen.getmaxyx()
        center_y = max_height // 2
        center_x = max_width // 2

        title_x = center_x - len(self._title) // 2
        title_y = center_y - 2
        input_listener = InputListener(screen)

        title_text = DisplayTextFactory.create(screen=screen, coords=[title_y, title_x], animate=True)
        title_text.display(self._title, format_options=['bold'])
        input_listener.wait_for_input()

        self._display_animated_line(screen, title_x, center_y)
        input_listener.wait_for_input()

    def _display_animated_line(self, screen, x: int, y: int):

        line = DisplayTextFactory.create(screen=screen, coords=[y, x], animate=True, animation_delay=0.005)
        underline = "=" * self.title_length
        line.display(underline)

        for i in range(len(underline)):
            next_line = [c for c in underline]
            next_line[i] = ">"
            next_line[-i - 1] = "<"
            line.display("".join(next_line))

        line.shift_y_by(1)
        line.display(self.created_by)

    @property
    def title_length(self) -> int:
        return len(self._title)

    @property
    def created_by(self) -> str:
        return f"By {self._author}"


class InvalidBorder(Exception):
    ...
