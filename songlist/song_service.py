import re
from songlist.song import Song
from songlist.markdown.markdown_parser import MarkdownParser
from songlist.song_file import SongFile

class SongService:
    """A service to read and write song list files"""

    def __init__(self):
        self.markdown_parser = MarkdownParser()

    def get_song_file(self, file_path: str) -> SongFile:
        markdown = self.markdown_parser.parse(file_path)
        song = Song(
            markdown.front_matter['name'],
            markdown.front_matter['artist'],
            int(markdown.front_matter['skill'])
        )

        return SongFile(song, markdown)

