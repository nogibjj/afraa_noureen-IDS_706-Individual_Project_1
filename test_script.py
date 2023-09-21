"""test_script module"""
import sys
import pandas as pd

sys.path.append("/workspaces/afraa_noureen-IDS_706-Individual_Project_1/src")

import src.script as script
countries_info_df = pd.read_csv("world-data-2023.csv")

def test_script():
    """
    testing function for script.py
    """
    desc_countries = script.descriptive_stats_countries(countries_info_df)
    assert desc_countries["Birth Rate"]["mean"] == 20.214973544973546
    assert desc_countries["Life expectancy"]["max"] == 85.4
    assert desc_countries["Maternal mortality ratio"]["count"] == 181.0

    median, mean, std_deviation = script.infant_mortality_countries(countries_info_df)
    assert mean == 21.332804232804236
    assert median == 14.0
    assert std_deviation == 19.548058157595808

if __name__ == "__main__":
    test_script()
