from dataclasses import dataclass
from .song import Song
# TODO pull from package from .markdown.markdown_file import MarkdownFile

@dataclass
class SongFile:
    """Contains the extracted song and the source markdown file"""
    song: Song
    file: MarkdownFile
