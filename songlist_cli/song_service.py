import re
from markup_front_matter_parser import FrontMatterParserFactory, InvalidFrontMatterError
from .song import Song
from .song_file import SongFile

class SongService:
    """A service to read and write song list files"""

    def __init__(self):
        self.parser_factory = FrontMatterParserFactory()

    def get_song_file(self, file_path: str) -> SongFile | None:
        parser = self.parser_factory.get_parser(file_path)
        try:
            markdown = parser.parse()
        except InvalidFrontMatterError as e:
            print(f"{file_path} encountered an error: {str(e)}")
            return None

        song = Song(
            markdown.front_matter['name'],
            markdown.front_matter['artist'],
            int(markdown.front_matter['skill'])
        )

        return SongFile(song, markdown)

    def update_song_file(self, song_file: SongFile):
        with open(song_file.file.path, "w") as original_file:
            new_file_content = song_file.song.to_front_matter()
            body = song_file.file.content and song_file.file.content.raw

            if body:
                new_file_content += new_file_content

            original_file.write(new_file_content)


