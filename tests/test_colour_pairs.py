from copy import copy
from unittest.mock import Mock

import pytest

from src.colour import ColourPairs, TooManyColoursSpecified, ColourPair


class TestColourPairs:

    def test_reach_max_colours_raises_error(self):
        cp = ColourPairs()
        cp._init_colour_pair = Mock()
        cp.MAX_COLOURS = 1

        colour_a = ColourPair(1, 2)

        cp.get(colour_a)
        with pytest.raises(TooManyColoursSpecified):
            colour_b = ColourPair(1, 1)
            cp.get(colour_b)

    def test_get_cached_colour_pair(self):
        cp = ColourPairs()
        cp._init_colour_pair = Mock()

        colour = ColourPair(1, 1)
        cp.get(colour)
        cache_snapshot = copy(cp.cache)

        cp.get(colour)
        assert cp.cache == cache_snapshot

    def test_new_colour_pair_starts_at_one(self):
        cp = ColourPairs()
        cp._init_colour_pair = Mock()

        assert cp.get(ColourPair(1, 1)) == 1
