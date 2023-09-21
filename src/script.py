"""script module using common functions from lib.py"""
import sys
try:
    import lib
except ModuleNotFoundError:
    sys.path.insert(1, './src')
    import lib


def descriptive_stats_countries(countries_info_df):
    """
    Use common funtions from lib.py to generate descriptive statistics across 
    differnt metrics from countries worldwide.
    """
    desc_stats = lib.display_countries_info(countries_info_df)
    print("Descriptive Statistics of countries across the globe:\n")
    print(desc_stats)
    return desc_stats

def infant_mortality_countries(countries_info_df):
    """
    Use common functions from lib.py to generate descriptive statistics over 
    infnat moratlity rate worldwide.
    """
    highest_infant_mortality, median, mean, std_deviation = lib.infant_mortality(
        countries_info_df
        )

    print("Descriptive Statistics on Infant Mortality worldwide:")
    print("Mean (Infant Moratlity Rate) = ", mean)
    print("Median (Infant Moratlity Rate) = ", median)
    print("Standard Deviation (Infant Moratlity Rate) = ", std_deviation)
    print("\nDetails of the country with the highest infant mortality rate is: \n")
    print(highest_infant_mortality)
    return median, mean, std_deviation

def plot_birthrate_infantmortality(countries_info_df):
    """
    Use common functions from lib.py to generate scatter plot for 
    Birth Rate vs Infant Moratlity Rate
    """
    lib.plot_scatter(countries_info_df)
