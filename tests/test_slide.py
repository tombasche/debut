from unittest.mock import Mock

import pytest

from debut import Text, Slide
from debut.slide import InvalidBorder


class TestSlide:

    @pytest.fixture
    def slide_with_spy_mocks(self):
        s = Slide(
            heading="Hello",
            text=Text(["unit test text"])
        )
        s.max_height = 100
        s.max_width = 100
        s._display_factory_method = Mock()
        s._input_listener_class = Mock()
        s._display_border = Mock()
        s._display_body = Mock()
        s._display_heading = Mock()
        return s

    @pytest.fixture
    def slide_with_spy_mocks_and_border(self):
        s = Slide(
            heading="Hello",
            text=Text(["unit test text"]),
            border="+"
        )
        s.max_height = 100
        s.max_width = 100
        s._display_factory_method = Mock()
        s._input_listener_class = Mock()
        s._display_border = Mock()
        s._display_body = Mock()
        s._display_heading = Mock()
        return s

    def test_display_method_with_default_settings(self, slide_with_spy_mocks):

        slide_with_spy_mocks.display(screen=Mock())
        assert not slide_with_spy_mocks._display_border.called
        assert slide_with_spy_mocks._display_heading.called
        assert slide_with_spy_mocks._display_body.called

    def test_display_method_with_border(self, slide_with_spy_mocks_and_border):
        slide_with_spy_mocks_and_border.display(screen=Mock())
        assert slide_with_spy_mocks_and_border._display_border.called

    def test_invalid_border_raises_error(self):
        with pytest.raises(InvalidBorder):
            Slide(
                heading="Something",
                text=Text(["unit test text"]),
                border="invalid border"
            )
