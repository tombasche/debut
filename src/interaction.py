from curses import KEY_LEFT, KEY_RIGHT

SPACEBAR_ASCII = 32


class InputListener:

    def __init__(self, screen):
        self._screen = screen

    def wait_for_input(self):
        while True:
            keypress = int(self._screen.getch())
            if self.pressed_spacebar(keypress) or self.pressed_forward(keypress):
                return

    def pressed_spacebar(self, keypress: int) -> bool:
        return keypress == SPACEBAR_ASCII

    def pressed_back(self, keypress: int) -> bool:
        return keypress == KEY_LEFT

    def pressed_forward(self, keypress: int) -> bool:
        return keypress == KEY_RIGHT
