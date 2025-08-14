import unittest
from pathlib import Path
from songlist_cli.song_service import SongService
from songlist_cli.song import Song

class TestSongService(unittest.TestCase):
    def setUp(self):
        self.service = SongService()
        self.fixtures_dir = Path(__file__).parent / "fixtures/markdown"

    def test_able_to_parse_markdown_with_no_body(self):
        song_file = self.service.get_song_file(self.fixtures_dir / 'creep.md')

        self.assertEqual(song_file.file.path, self.fixtures_dir / 'creep.md')
        self.assertEqual(song_file.file.content, None)
        self.assertEqual(song_file.song, Song('Creep', 'Radiohead', 3))

    def test_able_to_parse_markdown_with_body(self):
        song_file = self.service.get_song_file(self.fixtures_dir / 'song_with_body.md')

        self.assertEqual(song_file.file.path, self.fixtures_dir / 'song_with_body.md')
        self.assertEqual(song_file.file.content.raw, 'data lies here\n<h1>hello world</h1>\n\nteehee\n')
        self.assertEqual(song_file.song, Song('Wild World', 'Cat Stevens', 3))
