"""test_main module"""
import lib
import pandas as pd

countries_info_df = pd.read_csv("world-data-2023.csv")

def test_main():
    """
    testing function for script.py
    """
    desc_countries = lib.display_contries_info(countries_info_df)
    assert

if __name__ == "__main__":
    test_main()
