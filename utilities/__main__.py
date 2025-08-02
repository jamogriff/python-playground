import code
from utilities.utilidec import log, profile
from utilities.change_directory import ChangeDirectory

if __name__ == "__main__":
    local_namespace = dict(globals(), **locals())
    code.interact(
        banner="Provides log and profile decorators in addition to a ChangeDirectory context manager",
        local=local_namespace,
    )
