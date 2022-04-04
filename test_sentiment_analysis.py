import pytest
from sentiment_analysis import *

MOOD_CASES = [
    # Check that a list of only sad words returns sad
    (["doubt", "fakin'", "breaks", "hurtin'", "miss", "fool"], "sad"),

    # Check that a list of only angsty words returns angst
    (["could've", "villain", "blindly", "turnt", "ego", "monster"], "angst"),

    # Check that a list of only love words returns love
    (["love", "touch", "warm", "date", "lift", "heart"], "love"),

    # Check that a list of only happy words returns happy
    (["lights", "glitter", "fly", "delight", "hop", "sing"], "joy"),

    # Check that a list of only angry words reutrns anger
    (["police", "killer", "paranoid", "hate", "shit", "AK-40"], "anger"),

    # Check that a list with a majority sad words returns sad
    (["doubt", "fakin'", "breaks", "hurtin'", "miss", "sex"], "sad"),

    # Check that a list with a majority angsty words returns angst
    (["could've", "villain", "blindly", "turnt", "ego", "peace"], "angst"),

    # Check that a list with a majority love words returns love
    (["love", "touch", "warm", "date", "lift", "cages"], "love"),

    # Check that a list with a majority angry words returns angry
    (["police", "killer", "paranoid", "hate", "shit", "box"], "anger"),

    # Check that a list with a majority happy words returns happy
    (["lights", "glitter", "fly", "delight", "hop", "erased"], "joy"),

    # Check that a list with equal amounts of different moods returns the
    # mood of the first word

    (["fool", "broke", "bougie", "lovely", "crown", "doubt"], "sad"),

]

TOTALS_CASES = [
    # Check that a dictionary with 4 angry songs, 2 love songs, 1 happy song
    # 6 sad songs, and 1 angst song returns a list of [4, 2, 1, 6, 1]

    # Check that an empty dictionary returns a list of [0, 0, 0, 0, 0]

    # Check that a dictionary of 3 angry songs returns [3, 0, 0 ,0 ,0]

    # Check that a dictionary of 5 love songs returns [0, 5, 0 ,0 ,0]

    # Check that a dictionary of 1 happy song returns [0, 0, 1, 0, 0]

    # Check that a dictionary of 2 sad songs returns [0, 0, 0, 2, 0]

    # Check that a dictionary of 3 angsty songs returns [0, 0, 0, 0, 3]

]

