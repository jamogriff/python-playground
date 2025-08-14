import os
from .song_service import SongService
from .song_file import SongFile

class Cli:

    def list_songs(self, directory: str):
        if not directory.endswith('/'):
            directory += '/'

        files = os.listdir(directory)
        files_with_pathes = [directory + f for f in files]

        song_files = {}
        song_service = SongService()
        for index, file in enumerate(files_with_pathes):
            song_file = song_service.get_song_file(file) 

            if song_file:
                song_files[index] = song_file

        # List the song files and prompt user to select one
        print(f"{len(song_files)} song files found:")
        for index in song_files:
            print(f"- [{index}] {song_files[index].song.name} by {song_files[index].song.artist}")

        # Subsequent operations will be done on a single song file
        selected_song_id = self._get_valid_id_from_user(list(song_files.keys()))
        selected_song_file = song_files[int(selected_song_id)]
        print(f'Now editing {selected_song_file.song.name}')

        # A dict of a song's properties with an associated on the fly ID
        # Right now we only support changing the skill property
        valid_properties = {i: prop for i, prop in enumerate(selected_song_file.song.__dict__) if prop == 'skill'}
        for key, value in valid_properties.items():
            print(f"- [{key}] {value.capitalize()}")

        selected_property_id = self._get_valid_id_from_user(list(valid_properties.keys()))

        if valid_properties[selected_property_id] == 'skill':
            valid_values = [n for n in range(1, 7)]
        else:
            raise NotImplementedError('Only song skills can be modified')

        print(f'You may update the skill below')
        selected_value = self._get_valid_id_from_user(valid_values)
        setattr(selected_song_file.song, valid_properties[selected_property_id], selected_value)
        song_service.update_song_file(selected_song_file)

        print(f"Successfully updated {selected_song_file.file.path}")


    def _get_valid_id_from_user(self, valid_ids: list[int]) -> int:
        prompt = f"Enter a number to continue: "
        id_input = input(prompt)
        while int(id_input) not in valid_ids:
            id_input = input(prompt)
            # TODO: add warning and count mistakes. Boot after 3 to prevent faffing around

        return int(id_input)
