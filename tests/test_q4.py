"""HW7 Question 4 Tests"""

import sys
from unittest.mock import MagicMock, patch

import pandas as pd

sys.path.append('.')
from src.q4 import plot_long_case_rate, long_case_rate

class TestPlotLongCaseRate:
    """Tests for the plot_long_case_rate function."""

    def test_correct_numbers_are_passed_to_plot(self) -> None:
        """Test that the correct numbers are passed to the plot function."""
        data = {
            "Neighborhood": ["A", "A", "B", "B", "B", "C", "C", "C", "C"],
            "days_open": [9, 9, 9, 9, 9, 0, 0, 0, 0]
        }
        df = pd.DataFrame(data)
        mocked_percentages = {
            "N1": 12.5,
            "N2": 50.0,
            "N3": 87.5
        }

        mock_plt = MagicMock()
        with patch("src.q4.long_case_rate",
                   return_value=mocked_percentages), \
             patch("src.q4.plt", new=mock_plt):
            plot_long_case_rate(df)

        assert mock_plt.bar.call_count == 1
        args, kwargs = mock_plt.bar.call_args

        expected_neighborhoods = ["N1", "N2", "N3"]
        expected_percentages = [12.5, 50.0, 87.5]

        # Accept either positional args or named kwargs for x/y.
        if len(args) >= 2:
            neighborhoods_arg = args[0]
            percentages_arg = args[1]
        else:
            neighborhoods_arg = kwargs.get("x")
            percentages_arg = kwargs.get("height")

        assert neighborhoods_arg == expected_neighborhoods
        assert percentages_arg == expected_percentages

    def test_axes_and_overall_plot_are_labelled(self) -> None:
        """Test that the x-axis and y-axis are labeled, and the overall plot has a title."""
        data = {
            "Neighborhood": ["A", "A", "B", "B", "B", "C", "C", "C", "C"],
            "days_open": [9, 9, 9, 9, 9, 0, 0, 0, 0]
        }
        df = pd.DataFrame(data)
        mock_plt = MagicMock()
        with patch("src.q4.plt", new=mock_plt):
            plot_long_case_rate(df)

        assert mock_plt.xlabel.call_count == 1
        assert mock_plt.ylabel.call_count == 1
        assert mock_plt.title.call_count == 1
