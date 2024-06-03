import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Load data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original data')

    # Perform linear regression on the entire dataset
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create a range of years from the start year to 2050
    years_extended = pd.Series(range(1880, 2051))

    # Calculate the line of best fit
    sea_level_predicted = intercept + slope * years_extended

    # Plot the line of best fit
    plt.plot(years_extended, sea_level_predicted, color='red', label='Fit 1880-2050')

    # Create a dataframe from the year 2000 to the most recent year
    df_recent = df[df['Year'] >= 2000]

    # Perform linear regression on the recent dataset
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    # Calculate the line of best fit for the recent data
    sea_level_predicted_recent = intercept_recent + slope_recent * years_extended

    # Plot the line of best fit for recent data
    plt.plot(years_extended, sea_level_predicted_recent, color='green', label='Fit 2000-2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()
