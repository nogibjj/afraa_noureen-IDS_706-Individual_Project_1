"""main module"""
import pandas as pd
import matplotlib.pyplot as plt

def display_contries_info(countries_info_df):
    """
    Display basic info about all countries worldwide - covering a wide range of indicators 
    and attributes such as demographic statistics, economic indicators, environmental factors, 
    healthcare metrics and education statistics.
    """
    return countries_info_df.describe()

def plot_scatter(countries_info_df):
    """
    Function to plot Scatter plot for Birth Rate vs Infant Mortality Rate
    """
    countries_info_df.plot.scatter(
    x="Birth Rate",
    y="Infant mortality",
    title="Birth Rate vs Infant Mortality Rate",
    xlabel="Birth Rate",
    ylabel="Infant Mortality Rate",
    )
    plt.show()

def infant_mortality(countries_info_df):
    """
    Display descriptive statistics related to infant mortality rate and 
    find out the country with the highest Infant Mortality Rate
    """
    high_infant_mortality_df = countries_info_df.query("`Infant mortality` == `Infant mortality`.max()")
    median = countries_info_df["Infant mortality"].median()
    mean = countries_info_df["Infant mortality"].mean()
    std_deviation = countries_info_df["Infant mortality"].std()

    return high_infant_mortality_df, median, mean, std_deviation
