
import pytest

from src.display import DisplayString


@pytest.mark.parametrize('format_options, expected', [
    (['bold', 'underline'], DisplayString.decoration['bold'] | DisplayString.decoration['underline']),
    (['underline', 'bold'], DisplayString.decoration['underline'] | DisplayString.decoration['bold']),
    (['bold'], DisplayString.decoration['bold']),
    (['bold', 'red'], DisplayString.decoration['bold'] | DisplayString.colors['red']),
])
def test_combine_format_options(format_options, expected):
    assert DisplayString.combine_options(0, format_options) == expected, f"Expected the bitwise OR of {format_options}"
