"""test_main module"""
import main


def test_main():
    """
    testing function for main
    """
    highest_votes = main.display_highest_votes()
    # print(highest_votes.loc[0,"vote_count"])
    assert highest_votes.loc[0, "vote_count"] == 18448
    # print(highest_votes.loc[1,"vote_count"])
    assert highest_votes.loc[1, "vote_count"] == 24376


if __name__ == "__main__":
    test_main()
