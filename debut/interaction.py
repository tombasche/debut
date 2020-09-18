from curses import KEY_LEFT, KEY_RIGHT

SPACEBAR_ASCII = 32
BACK = KEY_LEFT
FORWARD = KEY_RIGHT


class InputListener:

    def __init__(self, screen):
        self._screen = screen

    def wait_for_input(self):
        while True:
            keypress = self.get_input()
            if self.pressed_spacebar(keypress) or self.pressed_forward(keypress):
                return

    def get_input(self) -> int:
        return int(self._screen.getch())

    def pressed_spacebar(self, keypress: int) -> bool:
        return keypress == SPACEBAR_ASCII

    def pressed_back(self, keypress: int) -> bool:
        return keypress == BACK

    def pressed_forward(self, keypress: int) -> bool:
        return keypress == FORWARD
