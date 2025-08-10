import re
from .song import Song
# TODO pull from package from songlist.markdown.markdown_parser import MarkdownParser
from .song_file import SongFile

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

    def update_song_file(self, song_file: SongFile):
        with open(song_file.file.path, "w") as original_file:
            new_file_content = song_file.song.to_front_matter() + song_file.file.body
            original_file.write(new_file_content)


