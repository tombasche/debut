from curses import start_color, use_default_colors, initscr, newwin, noecho, echo


class ScreenInterface:

    def __init__(self):
        self._screen = None

        self.color_enabled = False
        self.keypad_enabled = False
        self.echo_enabled = True

    @property
    def screen(self):
        assert self._screen
        return self._screen

    def new(self):
        self._create_screen()

    def _create_screen(self):
        self._screen = self.new_window()

        self.enable_colours()
        self.color_enabled = True

        self.enable_keypad()
        self.keypad_enabled = True

        self.disable_echo()
        self.echo_enabled = False

    def new_window(self):
        return newwin(*initscr().getmaxyx(), 0, 0)

    def enable_colours(self):
        start_color()
        use_default_colors()

    def enable_keypad(self):
        self._screen.keypad(True)

    def toggle_echo(self):
        if self.echo_enabled:
            noecho()
        else:
            echo()

    def enable_echo(self):
        self.echo_enabled = True
        echo()

    def disable_echo(self):
        self.echo_enabled = False
        noecho()

    def clear(self):
        self.screen.clear()
        self.screen.refresh()

    def __enter__(self):
        self.new()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.enable_echo()
        self.echo_enabled = True
