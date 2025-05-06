# [Sea Level Predictor](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/sea-level-predictor)
You will be [working on this project with our Gitpod starter code](https://gitpod.io/?autostart=true#https://github.com/freeCodeCamp/boilerplate-sea-level-predictor/).

We are still developing the interactive instructional part of the Python curriculum. For now, here are some videos on the freeCodeCamp.org YouTube channel that will teach you everything you need to know to complete this project:

* [Python for Everybody Video Course](https://www.freecodecamp.org/news/python-for-everybody/) (14 hours)
* [How to Analyze Data with Python Pandas](https://www.freecodecamp.org/news/how-to-analyze-data-with-python-pandas/) (10 hours)

You will analyze a dataset of the global average sea level change since 1880. You will use the data to predict the sea level change through year 2050.

Use the data to complete the following tasks:

* Use Pandas to import the data from `epa-sea-level.csv`.
* Use matplotlib to create a scatter plot using the `Year` column as the x-axis and the `CSIRO Adjusted Sea Level` column as the y-axis.
* Use the `linregress` function from `scipy.stats` to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
* Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
* The x label should be `Year`, the y label should be `Sea Level (inches)`, and the title should be `Rise in Sea Level`.

The boilerplate also includes commands to save and return the image.

## Development
Write your code in `sea_level_predictor.py`. For development, you can use `main.py` to test your code.

## Testing
The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for your convenience.

## Submitting
Copy your project's URL and submit it to freeCodeCamp.

## Data Source
[Global Average Absolute Sea Level Change](https://datahub.io/core/sea-level-rise), 1880-2014 from the US Environmental Protection Agency using data from CSIRO, 2015; NOAA, 2015.

# Code
```python
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')

    # Create first line of best fit
    line1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = range(1880, 2051)
    ax.plot(x1, line1.slope * x1 + line1.intercept)

    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    line2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    x2 = range(2000, 2051)
    ax.plot(x2, line2.slope * x2 + line2.intercept)

    # Add labels and title
    ax.set(title='Rise in Sea Level', xlabel='Year', ylabel='Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
```
### Sea Level Plot
![sea_level_plot](https://github.com/user-attachments/assets/cd5f25d2-6e33-4615-8e86-677a5c8fe99e)

## Test Result Screenshot
![Test result screenshot](https://github.com/user-attachments/assets/5d217dac-f972-4709-8f10-5e0eee6a84ec)
