"""HW7 Question 4

311 is a non-emergency service request system used by various cities to track and manage public 
service issues such as potholes, graffiti, broken streetlights, and other non-emergency public 
concerns. In this question, we will anallyze data about how long 311 cases stay open in various 
neighborhoods.

There are two files in the `data` folder. They are formatted versions of data from these websites:
Oakland/San Francisco: https://data.sfgov.org/City-Infrastructure/311-Cases/vw6y-z8j6/data_preview
Boston: https://data.boston.gov/dataset/311-service-requests
This question should work with data from either of these files as input.

Write a function called `plot_percentage_above_average_per_neighborhood` that displays a bar graph
showing, for each neighborhood, the percentage of cases that stay open for longer than the average
number of days that any case stays open. It should take an argument for a dataframe containing the
311 cases data. It should also take two optional arguments:
- `neighborhood_column`: The column name for neighborhoods. Default: "Neighborhood".
- `days_open_column`: The column name for days open. Default: "days_open".
If the specified columns are not present in the dataframe, the function should raise a KeyError.
In the bar graph, make sure to specify the x- and y-axis labels, and the overall title of the 
plot.

To help split up complex functionality into helper functions, you should also write a function 
called `percentage_above_average_per_neighborhood` that calculates the percentage of 
above-average-open cases for each neighborhood. It should return a dictionary where the 
keys are neighborhood names and the values are the corresponding percentages. (Its parameters
should be the same three as `plot_percentage_above_average_per_neighborhood` and it should also 
raise a KeyError if the specified columns are not present in the dataframe.)

You are not required to write tests for `plot_percentage_above_average_per_neighborhood` (they 
are provided), but you should write tests for `percentage_above_average_per_neighborhood`.
"""

import pandas as pd
import matplotlib.pyplot as plt
