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

        self._screen_interface = ScreenInterface()

    def present(self):

        with self._screen_interface as si:
            while self.current_index <= self.last_slide_index:
                s = self._slides[self.current_index]
                self.inject_page_number(s)
                self.inject_screen_size(si, s)
                s.display(si.screen)
                self.navigate(si.screen)
                self.clear(si)

    def inject_page_number(self, slide: Slide):
        if self._show_page_number:
            slide.page_number = str(self.current_index)

    def inject_screen_size(self, screen_interface: ScreenInterface, slide: Slide):
        height, width = screen_interface.screen_dimensions
        slide.max_height = height
        slide.max_width = width

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

    def clear(self, screen_interface: ScreenInterface):
        screen_interface.clear()
