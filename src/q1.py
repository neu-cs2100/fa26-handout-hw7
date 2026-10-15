"""HW7 Question 1

Write a function called `calculate_statistics` that takes a list of numbers and 
returns a dictionary containing these statistics:
- mean
- median
- variance
- min
- max

The function should also have an optional argument for whether to ignore outliers, which we define
as numbers that are more than three standard deviations away from the list's mean. The default 
value for this argument should be `False`.

If any statistic cannot be computed (e.g., if the list is empty), the statistic's value should be
None.

Example usage:

numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 100.0]
calculate_statistics(numbers)
    # {'mean': 19.1666666668, 'median': 3.5, 'variance': 1920.9666666666667, 'min': 1, 'max': 100}
calculate_statistics(numbers, ignore_outliers=True)
    # {'mean': 3.0, 'median': 3.0, 'variance': 2.5, 'min': 1, 'max': 5}
calculate_statistics([])
    # {'mean': None, 'median': None, 'variance': None, 'min': None, 'max': None}

Make sure to write appropriate documentation and tests.
"""

from typing import Optional
import numpy as np
