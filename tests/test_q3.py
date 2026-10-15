"""HW7 Question 3 Tests"""

import sys
from types import ModuleType
from typing import Any
from unittest.mock import MagicMock, patch

sys.path.append('.')

mock_matplotlib: Any = ModuleType('matplotlib')
mock_pyplot: Any = ModuleType('pyplot')
mock_pyplot.hist = MagicMock()
mock_pyplot.show = MagicMock()
mock_matplotlib.pyplot = mock_pyplot
sys.modules.setdefault('matplotlib', mock_matplotlib)
sys.modules.setdefault('matplotlib.pyplot', mock_pyplot)

from src.q3 import draw_histogram

class TestDrawHistogram:
    """Tests for the draw_histogram function."""

    def _extract_hist_args(
            self, call_args: tuple[tuple[Any, ...], dict[str, Any]]
    ) -> tuple[list[float], int | list[float]]:
        """Extract the `numbers` and `bins` arguments from a call to matplotlib.pyplot.hist."""
        args, kwargs = call_args

        if args:
            numbers = args[0]
        else:
            numbers = kwargs['x']

        if len(args) > 1:
            bins = args[1]
        else:
            bins = kwargs['bins']

        return numbers, bins

    def test_draw_histogram_fixed_width_values(self) -> None:
        """Test that the draw_histogram function passes the right values to matplotlib 
        when asked to use fixed width bins."""
        numbers = [10.0, 20.0, 30.0, 40.0, 50.0]
        expected_bins = 4

        with patch('src.q3.plt.hist') as mock_hist, patch('src.q3.plt.show'):
            draw_histogram(numbers, bins=expected_bins, fixed_width=True)

        mock_hist.assert_called_once()
        called_numbers, called_bins = self._extract_hist_args(mock_hist.call_args)
        assert called_numbers == numbers
        assert called_bins == expected_bins

    def test_draw_histogram_fixed_size_values(self) -> None:
        """Test that the draw_histogram function passes the right values to matplotlib 
        when asked to use fixed size bins."""
        numbers = [8.0, 2.0, 7.0, 1.0, 6.0, 3.0, 5.0, 4.0]
        expected_bins = [1, 3, 5, 7, 8]

        with patch('src.q3.plt.hist') as mock_hist, patch('src.q3.plt.show'):
            draw_histogram(numbers, bins=4, fixed_width=False)

        mock_hist.assert_called_once()
        called_numbers, called_bins = self._extract_hist_args(mock_hist.call_args)
        assert called_numbers == numbers
        assert called_bins == expected_bins
