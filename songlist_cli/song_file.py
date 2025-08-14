from dataclasses import dataclass
from markup_front_matter_parser import MarkupFile
from .song import Song

@dataclass
class SongFile:
    """Contains the extracted song and the source markdown file"""
    song: Song
    file: MarkupFile
