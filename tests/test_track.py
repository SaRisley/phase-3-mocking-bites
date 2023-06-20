from lib.track import *

def test_matches_on_full_title():
    track = Track("Song", "Artist")
    assert track.matches("Song") == True

def test_matches_on_partial_title():
    track = Track("Good Song", "Great Artist")
    assert track.matches("Good") == True

def test_matches_on_full_artist():
    track = Track("Good Song", "Great Artist")
    assert track.matches("Great Artist") == True

def test_matches_on_partial_artist():
    track = Track("Good Song", "Great Artist")
    assert track.matches("Great") == True

def test_does_not_match():
    track = Track("Good Song", "Great Artist")
    assert track.matches("Bad") == False