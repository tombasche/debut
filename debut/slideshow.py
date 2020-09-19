from curses import initscr, noecho, start_color, newwin, use_default_colors, echo
from typing import List

from debut.interaction import InputListener
from debut.screen_interface import ScreenInterface
from debut.slide import Slide


class SlideShow:

    def __init__(self, slides: List[Slide], show_page_numbers=False):
        self._slides = slides
        self.screen = None

        self.current_index = 0
        self.last_slide_index = len(self._slides) - 1

        self._show_page_number = show_page_numbers

    def present(self):

        with ScreenInterface() as si:
            while self.current_index <= self.last_slide_index:
                s = self._slides[self.current_index]
                self.inject_page_number(s)
                s.display(si.screen)
                self.navigate(si.screen)
                si.clear()

    def inject_page_number(self, screen):
        if self._show_page_number:
            screen.page_number = str(self.current_index)

    def navigate(self, screen):
        listener = InputListener(screen)

        while True:
            key_press = int(screen.getch())
            if listener.pressed_spacebar(key_press) or listener.pressed_forward(key_press):
                self.current_index += 1
                break
            elif listener.pressed_back(key_press):
                if self.current_index > 0:
                    self.current_index = self.current_index - 1
                break
