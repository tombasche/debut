from curses import initscr, endwin, noecho, start_color, newwin
from typing import List

from src.interaction import NextAction
from src.slide import Slide


class SlideShow:

    def __init__(self, slides: List[Slide]):
        self._slides = slides

        self.screen = None

    def present(self):
        for slide in self._slides:
            self.initialise_screen()
            slide.display(self.screen)
            if self._can_move_to_next_slide():
                self.screen.clear()
                self.screen.refresh()
                endwin()

    def initialise_screen(self):
        global_screen = initscr()
        self.screen = newwin(*global_screen.getmaxyx(), 0, 0)
        start_color()
        noecho()

    def _can_move_to_next_slide(self):
        NextAction(self.screen).wait_for_input()
