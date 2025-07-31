import code
from jamolib.models.library import Library
from jamolib.models.book import Book
from jamolib.models.user import User

if __name__ == "__main__":
    local_namespace = dict(globals(), **locals())  # This is awesome
    code.interact(banner="Welcome to JamoLib", local=local_namespace)
