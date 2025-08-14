import code
from .cli import Cli

if __name__ == "__main__":
    # TODO: set this via ENV
    directory = 'songlist_cli/tests/fixtures/markdown'
    cli = Cli() 
    cli.list_songs(directory)
    # local_namespace = dict(globals(), **locals())  # This is awesome
    # code.interact(banner="Welcome to Songlist", local=local_namespace)
