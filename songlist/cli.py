import os
from songlist.song_service import SongService
from songlist.song_file import SongFile
#from utilities import ChangeDirectory

class Cli:

    def list_songs(self, directory: str):
        if not directory.endswith('/'):
            directory += '/'

        files = os.listdir(directory)
        files_with_pathes = [directory + f for f in files]

        song_files = {}
        song_service = SongService()
        for index, file in enumerate(files_with_pathes):
            song_files[index] = song_service.get_song_file(file) 

        print(f"{len(song_files)} song files found:")

        for index in song_files:
            print(f"- [{index}] {song_files[index].song.name} by {song_files[index].song.artist}")

        selected_song = input(f"Enter a number to edit: ")
        while int(selected_song) not in list(song_files.keys()):
            selected_song = input(f"Enter a number to edit: ")

        print(f'Now editing {song_files[int(selected_song)].song.name}')
        #TODO: input for skill




