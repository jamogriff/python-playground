from dataclasses import dataclass
from songlist.song import Song
from songlist.markdown.markdown_file import MarkdownFile

@dataclass
class SongFile:
    """Contains the extracted song and the source markdown file"""
    song: Song
    file: MarkdownFile
