from curses import initscr, endwin, noecho, start_color, newwin
from typing import List
from src.slide import Slide

SPACEBAR_ASCII = 32


class SlideShow:

    def __init__(self, slides: List[Slide]):
        self._slides = slides

        self.screen = None

    def present(self):
        for slide in self._slides:
            self.initialise_screen()
            slide.display(self.screen)
            if self._can_move_to_next_slide():
                screen.clear()
                screen.refresh()
                endwin()

    def initialise_screen(self):
        global_screen = initscr()
        max_height, max_width = global_screen.getmaxyx()
        self.screen = newwin(max_height, max_width, 0, 0)
        start_color()
        noecho()

    def _can_move_to_next_slide(self):
        moving_on = False
        while moving_on is False:
            keypress = self.screen.getch()
            if keypress == SPACEBAR_ASCII:
                moving_on = True
