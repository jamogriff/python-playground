import unittest
import json
from songlist.song import Song

class TestSong(unittest.TestCase):
    def test_song_can_be_serialized_to_json(self):
        song = Song('Hand on the Wheel', 'Willie Nelson', 3)
        song_json = song.to_json()

        self.assertEqual(json.loads(song_json), song.__dict__)

    def test_song_can_be_serialized_to_front_matter(self):
        song = Song('Hand on the Wheel', 'Willie Nelson', 3)
        song_front_matter = song.to_front_matter()
        expected = "---\nname: Hand on the Wheel\nartist: Willie Nelson\nskill: 3\n---\n"

        self.assertEqual(song_front_matter, expected)


