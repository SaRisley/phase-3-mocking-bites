from lib.music_library import *
from lib.track import *

def test_adds_and_lists_multi_tracks():
    library = MusicLibrary()
    track_1 = Track("Good Song", "Good Artist")
    track_2 = Track("Great Song", "Great Artist")
    library.add(track_1)
    library.add(track_2)
    assert library.tracks == [track_1, track_2]

def test_search_for_track_by_title():
    library = MusicLibrary()
    track_1 = Track("Title", "Artist1")
    track_2 = Track("Song", "Artist2")
    library.add(track_1)
    library.add(track_2)
    assert library.search("Song")== [track_2]

def test_search_for_track_by_partial_title():
    library = MusicLibrary()
    track_1 = Track("Title", "Artist1")
    track_2 = Track("Great Song", "Artist2")
    library.add(track_1)
    library.add(track_2)
    assert library.search("Song")== [track_2]
