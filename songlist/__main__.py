import code
from songlist.song import Song
from songlist.file_parser import FileParser
from songlist.song_service import SongService
from songlist.cli import Cli

if __name__ == "__main__":
    directory = 'songlist/tests/fixtures/markdown'
    cli = Cli() 
    cli.list_songs(directory)
    # local_namespace = dict(globals(), **locals())  # This is awesome
    # code.interact(banner="Welcome to Songlist", local=local_namespace)
