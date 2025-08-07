import re
from songlist.song import Song
from songlist.file_parser import FileParser

class SongService:
    """A service to read and write song list files"""

    def __init__(self):
        self.file_parser = FileParser()

    def get_song_from_file(self, file_path: str) -> Song:
        with open(file_path, "r") as file:
            file_ext = self.get_file_extension(file.name)

            if file_ext == ".md":
                obj = self.file_parser.parse_front_matter(file)
            elif file_ext == ".json":
                import warnings
                warnings.warn('No intention of supporting this.', DeprecationWarning)
                obj = self.file_parser.parse_json(file)
            else:
                raise RuntimeError(f'Parsing {file_ext} files is not implemented')

        return Song(obj['name'], obj['artist'], int(obj['skill']))
            

    def get_file_extension(self, file_name) -> str:
        """Returns file extension of a given file and will raise exception if none found.
        Example return string: .json"""
        match = re.search(r'\.(.+)', file_name)

        if not match:
            raise ValueError(f'{file_name} does not have a file type')

        return match.group()

