from unittest.mock import Mock

import pytest

from debut.display import DisplayTextFactory


class TestDisplayText:

    sample_text = "here be text"

    @pytest.fixture
    def mock_screen(self):
        screen = Mock()
        screen.getmaxyx.return_value = (300, 300)
        return screen

    @pytest.fixture
    def mock_colour_pairs(self):
        colour_pairs = Mock()
        colour_pairs.get.return_value = 1
        return colour_pairs

    def test_normal_display_text_without_options(self, mock_screen, mock_colour_pairs):
        text = DisplayTextFactory.create(
            screen=mock_screen,
            coords=[1, 2],
            colour_pairs=mock_colour_pairs
        )
        text.display_string = Mock()
        text.display(self.sample_text)
        text.display_string.assert_called_with(
            combined_options=1,
            coords=[1, 2],
            text=self.sample_text,
            screen=mock_screen
        )

    def test_normal_display_text_with_formatting_options(self, mock_screen, mock_colour_pairs):
        text = DisplayTextFactory.create(
            screen=mock_screen,
            coords=[1, 2],
            colour_pairs=mock_colour_pairs,
        )
        text.display_string = Mock()
        text.display(self.sample_text, format_options=['bold', 'underline'])
        text.display_string.assert_called_with(
            combined_options=2228225,
            coords=[1, 2],
            text=self.sample_text,
            screen=mock_screen
        )

    def test_animated_display_without_options(self, mock_screen, mock_colour_pairs):
        text = DisplayTextFactory.create(
            screen=mock_screen,
            coords=[1, 2],
            colour_pairs=mock_colour_pairs,
            animate=True
        )
        text.display_string = Mock()
        text.display(self.sample_text)
        assert text.display_string.call_count == 10

    def test_animated_display_with_custom_animation_delay(self, mock_screen, mock_colour_pairs):

        animation_delay = 0.005
        text = DisplayTextFactory.create(
            screen=mock_screen,
            coords=[1, 2],
            colour_pairs=mock_colour_pairs,
            animate=True,
            animation_delay=animation_delay
        )
        text.delay = Mock()
        text.display_string = Mock()
        text.display(self.sample_text)
        assert text.display_string.call_count == 10

        text.delay.assert_called_with(animation_delay)
