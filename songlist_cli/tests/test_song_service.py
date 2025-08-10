import unittest
from songlist_cli.song_service import SongService
from songlist_cli.song import Song

class TestSongService(unittest.TestCase):
    def test_able_to_parse_markdown_with_no_body(self):
        service = SongService()
        song_file = service.get_song_file('songlist/tests/fixtures/markdown/creep.md')

        self.assertEqual(song_file.file.path, 'songlist/tests/fixtures/markdown/creep.md')
        self.assertEqual(song_file.file.body, '')
        self.assertEqual(song_file.song, Song('Creep', 'Radiohead', 3))

    def test_able_to_parse_markdown_with_body(self):
        service = SongService()
        song_file = service.get_song_file('songlist/tests/fixtures/markdown/song_with_body.md')

        self.assertEqual(song_file.file.path, 'songlist/tests/fixtures/markdown/song_with_body.md')
        self.assertEqual(song_file.file.body, 'data lies here\n<h1>hello world</h1>\n\nteehee\n')
        self.assertEqual(song_file.song, Song('Wild World', 'Cat Stevens', 3))
