
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

    (["drowning", "broke", "bougie", "lovely", "crown", "doubt"], "sad"),

]


TOTALS_CASES = [
   
    # Check that an empty dictionary returns a list of [0, 0, 0, 0, 0]
    ({}, [0,0,0,0,0]),
    # Check that a dictionary of 3 angry songs returns [3, 0, 0 ,0 ,0]
    ({1: ["police", "killer", "paranoid", "hate", "shit", "box", "anger"], \
      2: ["police", "killer", "paranoid", "hate", "shit", "box", "anger"], \
      3: ["police", "killer", "paranoid", "hate", "shit", "box", "anger"]},\
      [3,0,0,0,0]),
    # Check that a dictionary of 1 love songs returns [0, 1, 0 ,0 ,0]
    ({1:["love", "touch", "warm", "date", "lift", "cages", "love"]},\
     [0,1,0,0,0]),
    # Check that a dictionary of 1 happy song returns [0, 0, 1, 0, 0]
    ({1:["lights", "glitter", "fly", "delight", "hop", "sing", "joy"]},\
     [0,0,1,0,0]),
    # Check that a dictionary of 1 sad songs returns [0, 0, 0, 1, 0]
    ({1: ["doubt", "fakin'", "breaks", "hurtin'", "miss", "fool", "sad"]},\
      [0,0,0,1,0]),
    # Check that a dictionary of 1 angsty songs returns [0, 0, 0, 0, 1]
    ({1:["could've", "villain", "blindly", "turnt", "ego", "peace", "angst"]},\
     [0,0,0,0,1]),

    # Check that a dictionary with 1 of each type returns [1,1,1,1,1]
    ({1:["police", "killer", "paranoid", "hate", "shit", "box", "anger"],\
     2: ["love", "touch", "warm", "date", "lift", "cages", "love"],\
     3:["lights", "glitter", "fly", "delight", "hop", "sing", "joy"],\
     4: ["doubt", "fakin'", "breaks", "hurtin'", "miss", "fool", "sad"],\
     5: ["could've", "villain", "blindly", "turnt", "ego", "peace", "angst"]},\
     [1,1,1,1,1])

]

def test_mood_categorizer():
    for item in MOOD_CASES:
        assert(mood_categorizer(item[0]) == item[1])


def test_totals():
    for item in TOTALS_CASES:
        assert(totals(item[0]) == item[1])