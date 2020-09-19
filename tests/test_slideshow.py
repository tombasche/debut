from unittest.mock import Mock, MagicMock

from debut import SlideShow


class TestSlideshow:

    def test_present(self):

        def increment_index_side_effect(arg):
            slideshow.current_index += 1

        slideshow = SlideShow(slides=[Mock(), Mock()])
        slideshow._screen_interface = MagicMock()
        slideshow.inject_screen_size = Mock()
        slideshow.clear = Mock()
        slideshow.navigate = Mock(
            side_effect=increment_index_side_effect
        )
        slideshow.present()
        assert slideshow.clear.called

    def test_last_slide_index(self):
        slideshow = SlideShow(slides=[Mock(), Mock()])
        assert slideshow.last_slide_index == 1

    def test_slides_all_display(self):

        def increment_index_side_effect(arg):
            slideshow.current_index += 1

        slide_1 = Mock()
        slide_2 = Mock()
        slideshow = SlideShow(slides=[slide_1, slide_2])
        slideshow._screen_interface = MagicMock()
        slideshow.inject_screen_size = Mock()
        slideshow.clear = Mock()
        slideshow.navigate = Mock(
            side_effect=increment_index_side_effect
        )
        slideshow.present()
        for slide in [slide_1, slide_2]:
            assert slide.display.called
