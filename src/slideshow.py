from curses import initscr, noecho, start_color, newwin
from typing import List

from src.interaction import InputListener
from src.slide import Slide


class SlideShow:

    def __init__(self, slides: List[Slide]):
        self._slides = slides
        self.screen = None

        self.current_index = 0
        self.last_slide_index = len(self._slides) - 1

    def present(self):

        self.initialise_screen()
        while self.current_index <= self.last_slide_index:
            self._slides[self.current_index].display(self.screen)
            self.navigate()
            self.clear()

    def initialise_screen(self):
        self.screen = newwin(*initscr().getmaxyx(), 0, 0)
        self.screen.keypad(True)
        start_color()
        noecho()

    def navigate(self):
        listener = InputListener(self.screen)

        while True:
            key_press = int(self.screen.getch())
            if listener.pressed_spacebar(key_press) or listener.pressed_forward(key_press):
                self.current_index += 1
                break
            elif listener.pressed_back(key_press):
                if self.current_index > 0:
                    self.current_index = self.current_index - 1
                break

    def clear(self):
        self.screen.clear()
        self.screen.refresh()
