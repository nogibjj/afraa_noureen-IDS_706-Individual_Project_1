"""test_lib module"""
import sys
import pandas as pd
import matplotlib.pyplot as plt

sys.path.append("/workspaces/afraa_noureen-IDS_706-Individual_Project_1/src")

import src.lib as lib
countries_info_df = pd.read_csv("world-data-2023.csv")

def test_display_countries_info():
    """
    testing function for display_countries_info()
    """
    desc_countries = lib.display_countries_info(countries_info_df)
    assert desc_countries["Birth Rate"]["mean"] == 20.214973544973546
    assert desc_countries["Life expectancy"]["max"] == 85.4
    assert desc_countries["Maternal mortality ratio"]["count"] == 181.0

def test_infant_mortality():
    """
    testing function for hinfant_mortality()
    """
    high_infant_mortality_df, median, mean, std_deviation = lib.infant_mortality(countries_info_df)
    assert high_infant_mortality_df["Birth Rate"][33] == 35.35
    assert mean == 21.332804232804236
    assert median == 14.0
    assert std_deviation == 19.548058157595808

def test_plot_scatter():
    """
    test the scatter plot function
    """
    lib.plot_scatter(countries_info_df)
    scatter = plt.gcf()
    assert len(scatter.axes) > 0

if __name__ == "__main__":
    test_display_countries_info()
    test_infant_mortality()
    test_plot_scatter()
