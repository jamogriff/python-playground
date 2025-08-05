from songlist.song import Song

class SongService:
    """A service to read and write song list files"""

    def get_song_from_file(file_path: str) -> Song:
        with open(file_path, "w") as file:
            pass
            
