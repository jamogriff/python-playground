import code
from utils.utils import Utilities

if __name__ == "__main__":
    local_namespace = dict(globals(), **locals())
    code.interact(
        banner=Utilities.__name__ + ": " + Utilities.__doc__,
        local=local_namespace
    )
