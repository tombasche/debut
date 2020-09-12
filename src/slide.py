from curses import curs_set

from src.display import DisplayText
from src.interaction import InputListener
from src.text import Text


class Slide:

    def __init__(self, heading: str, text: Text, advance_on_input=True, animated_heading=False):
        self._heading = heading
        self._text = text
        self.advance_on_input = advance_on_input

        self._animated_heading = animated_heading

    def display(self, screen):

        input_listener = None
        if self.advance_on_input:
            input_listener = InputListener(screen)
        self._display_heading(screen, input_listener, )

        slide_body = DisplayText(screen=screen, coords=[3, 3], input_listener=input_listener)
        slide_body.display(text=self._text.render())

        self._display_nav_indicator(screen)

    def _display_heading(self, screen, input_listener):

        heading_text = DisplayText(screen=screen, coords=[0, 5])
        heading_text.display(
            text=self._heading,
            format_options=['bold', 'underline'],
            highlight_color='blue',
            animate=self._animated_heading
        )

        underline = DisplayText(screen=screen, coords=[1, 5])
        underline.display(text="=" * len(self._heading), animate=False)

        if input_listener:
            input_listener.wait_for_input()

    def _display_nav_indicator(self, screen):
        max_height, _ = screen.getmaxyx()
        nav_indicator = DisplayText(screen=screen, coords=[max_height - 1, 1])
        nav_indicator.display(text="<< | >> ", highlight_color='red', text_color='white', animate=False)


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

        title_text = DisplayText(screen=screen, coords=[title_y, title_x])
        title_text.display(self._title, format_options=['bold'], highlight_color='blue', text_color='white')
        input_listener.wait_for_input()

        self._display_animated_line(screen, title_x, center_y)
        input_listener.wait_for_input()

    def _display_animated_line(self, screen, x: int, y: int):

        line = DisplayText(screen=screen, coords=[y, x])
        underline = "=" * self.title_length
        line.display(underline)

        curs_set(0)
        for i in range(len(underline)):
            next_line = [c for c in underline]
            next_line[i] = ">"
            next_line[-i - 1] = "<"
            line.display("".join(next_line), animate=True, custom_character_delay=0.005)

        line.shift_y_by(1)
        line.display(self.created_by)
        curs_set(1)

    @property
    def title_length(self) -> int:
        return len(self._title)

    @property
    def created_by(self) -> str:
        return f"By {self._author}  "

