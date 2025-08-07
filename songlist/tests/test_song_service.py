import unittest
from songlist.song_service import SongService
from songlist.song import Song

class TestSongService(unittest.TestCase):
    def test_able_to_parse_markdown_song(self):
        service = SongService()
        song = service.get_song_from_file('songlist/tests/fixtures/markdown/creep.md')

        self.assertEqual(song, Song('Creep', 'Radiohead', 3))

    def test_able_to_parse_json_song(self):
        service = SongService()
        song = service.get_song_from_file('songlist/tests/fixtures/json/creep.json')

        self.assertEqual(song, Song('Creep', 'Radiohead', 3))

