
import pytest

from src.display import DisplayText


@pytest.mark.parametrize('format_options, expected', [
    (['bold', 'underline'], DisplayText.decoration['bold'] | DisplayText.decoration['underline']),
    (['underline', 'bold'], DisplayText.decoration['underline'] | DisplayText.decoration['bold']),
    (['bold'], DisplayText.decoration['bold']),
    (['bold', 'red'], DisplayText.decoration['bold'] | DisplayText.colors['red']),
])
def test_combine_format_options(format_options, expected):
    assert DisplayText.combine_options(0, format_options) == expected, f"Expected the bitwise OR of {format_options}"
