import os
from songlist.song_service import SongService
#from utilities import ChangeDirectory

class Cli:

    def list_songs(self, directory: str):
        if not directory.endswith('/'):
            directory += '/'

        files = os.listdir(directory)
        files_with_pathes = [directory + f for f in files]

        songs = {}
        song_service = SongService()
        for index, file in enumerate(files_with_pathes):
            songs[index] = song_service.get_song_from_file(file)

        print(f"{len(songs)} song files found:")

        for index in songs:
            print(f"- [{index}] {songs[index].name} by {songs[index].artist}")

        selected_song = input(f"Enter a number to edit: ")
        while int(selected_song) not in list(songs.keys()):
            selected_song = input(f"Enter a number to edit: ")

        print(f'Now editing {songs[int(selected_song)].name}')
        #TODO: input for skill




