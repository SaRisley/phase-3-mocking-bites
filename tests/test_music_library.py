from unittest.mock import Mock
from lib.music_library import *

def test_search_by_keyword():
    library = MusicLibrary()
    fake_matching = Mock()
    fake_matching.matches.return_value = True
    library.add(fake_matching)
    fake_not_matching = Mock()
    fake_not_matching.matches.return_value = False
    library.add(fake_not_matching)
    assert library.search("Great") == [fake_matching]

def test_tracks_initially_empty():
    library = MusicLibrary()
    assert library.tracks == []

def test_tracks_added_and_listed():
    library = MusicLibrary()
    track_1 = Mock()
    track_2 = Mock()
    track_3 = Mock()
    library.add(track_1)
    library.add(track_2)
    library.add(track_3)
    assert library.tracks == [track_1, track_2, track_3]
