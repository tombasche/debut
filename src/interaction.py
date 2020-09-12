
SPACEBAR_ASCII = 32


class InputListener:

    continue_character = SPACEBAR_ASCII

    def __init__(self, screen):
        self._screen = screen

    def wait_for_input(self):
        moving_on = False
        while moving_on is False:
            keypress = self._screen.getch()
            if keypress == self.continue_character:
                moving_on = True
