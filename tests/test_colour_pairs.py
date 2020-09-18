from copy import copy
from unittest.mock import Mock

import pytest

from debut.colour import ColourPairs, TooManyColoursSpecified, ColourPair


class TestColourPairs:

    @pytest.fixture
    def mocked_colour_pairs(self):
        cp = ColourPairs()
        cp._init_colour_pair = Mock()
        cp._retrieve_color_pair = Mock()
        return cp

    def test_reach_max_colours_raises_error(self, mocked_colour_pairs):
        mocked_colour_pairs.MAX_COLOURS = 1

        colour_a = ColourPair(1, 2)

        mocked_colour_pairs.get(colour_a)
        with pytest.raises(TooManyColoursSpecified):
            colour_b = ColourPair(1, 1)
            mocked_colour_pairs.get(colour_b)

    def test_get_cached_colour_pair(self, mocked_colour_pairs):

        colour = ColourPair(1, 1)
        mocked_colour_pairs.get(colour)
        cache_snapshot = copy(mocked_colour_pairs.cache)

        mocked_colour_pairs.get(colour)
        assert mocked_colour_pairs.cache == cache_snapshot
