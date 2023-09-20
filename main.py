"""main module"""
import pandas as pd
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport


def display_highest_votes():
    """
    Display basic info about movies dataset
    """
    movies_df = pd.read_csv("MoviesTopRated.csv")
    vote_df = movies_df.query("vote_average == vote_average.max()")
    print("Summary Statistics of the Top Rated Movies Dataset:\n")
    print(movies_df.describe())
    movies_df.plot.scatter(
        x="popularity",
        y="vote_average",
        title="popularity vs vote_average graph",
        xlabel="Popularity",
        ylabel="Average Ratings out of 10",
    )
    plt.show()
    print("\nDetails of the movies that were given the highest votes are: \n")
    print(vote_df)
    pdf_report_generator(movies_df)
    return vote_df


def pdf_report_generator(df):
    profile = ProfileReport(df, title="Summary Report")
    profile.to_file("Summary_Report.html")
