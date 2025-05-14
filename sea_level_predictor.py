import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    plt.figure()

    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label='CSIRO Sea Level Data')


    # Create first line of best fit
    # Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. 
    # Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to 
    # predict the sea level rise in 2050.
    fit_line_1 = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    x1 = pd.Series(range(1880, 2051))
    y1 = fit_line_1.slope * x1 + fit_line_1.intercept
    plt.plot(x1, y1, 'r', label='Overall trend 1880-2050')


    # Create second line of best fit
    # Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. 
    # Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues 
    # as it has since the year 2000.
    recent_data = data[data['Year'] >= 2000]
    fit_line_2 = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    x2 = pd.Series(range(2000, 2051))
    y2 = fit_line_2.slope * x2 + fit_line_2.intercept
    plt.plot(x2, y2, 'g', label='Trend 2000-2050')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
