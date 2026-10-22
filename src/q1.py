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

numbers = [1.0, 1.0, 1.0, 1.0, 1.0, 100.0]
calculate_statistics(numbers)
    # {'mean': 17.5, 'median': 1.0, 'variance': 1361.25, 'min': 1, 'max': 100}
calculate_statistics(numbers, ignore_outliers=True)
    # {'mean': 1.0, 'median': 1.0, 'variance': 0, 'min': 1, 'max': 1}
calculate_statistics([])
    # {'mean': None, 'median': None, 'variance': None, 'min': None, 'max': None}

Make sure to write appropriate documentation and tests.
"""

from typing import Optional
import numpy as np
