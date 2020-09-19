from unittest.mock import Mock

import pytest

from debut.screen_interface import ScreenInterface


class TestScreenInterface:

    @pytest.fixture
    def screen_interface(self):
        interface = ScreenInterface()
        interface._screen = Mock()
        interface.new_window = Mock()
        interface.enable_colours = Mock()
        interface.disable_echo = Mock()
        interface.enable_echo = Mock()
        return interface

    def test_create_screen(self, screen_interface):

        with screen_interface as si:
            assert si.color_enabled
            assert si.keypad_enabled
            assert si.echo_enabled is False

    def test_quitting_of_screen_enables_echo(self, screen_interface):

        with screen_interface as si:
            ...

        assert si.echo_enabled
