from songlist.mixins.json_mixin import JsonMixin
from songlist.mixins.front_matter_mixin import FrontMatterMixin

class Song(JsonMixin, FrontMatterMixin):

    def __init__(self, name: str, artist: str, skill: int):
        self.name = name
        self.artist = artist
        self.skill = skill

    def __eq__(self, other) -> bool:
        if not isinstance(other, Song):
            return NotImplemented
        return self.name == other.name and self.artist == other.artist
