from songlist.mixins.json_mixin import JsonMixin
from songlist.mixins.front_matter_mixin import FrontMatterMixin

class Song(JsonMixin, FrontMatterMixin):

    def __init__(self, name: str, artist: str, skill: int):
        self.name = name
        self.artist = artist
        self.skill = skill
