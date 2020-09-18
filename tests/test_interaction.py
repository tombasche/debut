from unittest.mock import Mock

import pytest

from debut.interaction import InputListener, SPACEBAR_ASCII, BACK, FORWARD


class TestInteraction:

    @pytest.fixture
    def mocked_input_listener(self):
        il = InputListener(
            screen=Mock()
        )
        return il

    def test_pressed_spacebar(self, mocked_input_listener):
        assert mocked_input_listener.pressed_spacebar(SPACEBAR_ASCII)

    def test_pressed_back(self, mocked_input_listener):
        assert mocked_input_listener.pressed_back(BACK)

    def test_pressed_forward(self, mocked_input_listener):
        assert mocked_input_listener.pressed_forward(FORWARD)

    def test_progression_on_correct_button_push(self, mocked_input_listener):
        mocked_input_listener.get_input = Mock(return_value=SPACEBAR_ASCII)
        assert mocked_input_listener.wait_for_input() is None
