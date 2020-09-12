from curses import initscr, endwin, noecho, start_color
from typing import List
from src.slide import Slide

SPACEBAR_ASCII = 32


class SlideShow:

    def __init__(self, slides: List[Slide]):
        self._slides = slides

        self.screen = None

    def present(self, screen=None):
        self.initialise_screen(screen)
        for slide in self._slides:

            slide.display(self.screen)
            if self._can_move_to_next_slide():
                screen.erase()
                screen.refresh()

    def initialise_screen(self, screen):
        self.screen = screen or initscr()
        start_color()
        noecho()

    def _can_move_to_next_slide(self):
        moving_on = False
        while moving_on is False:
            keypress = self.screen.getch()
            if keypress == SPACEBAR_ASCII:
                moving_on = True
