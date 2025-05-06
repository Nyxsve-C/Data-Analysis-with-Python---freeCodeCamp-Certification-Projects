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