from functools import wraps
import logging
import time

class Utilities:
    """A class for utility decorators. Create an instance by passing
    a log filename and the log level."""

    def __init__(self, log_file: str, log_level: str = 'DEBUG'):
        log_level = log_level.upper()
        numeric_level = getattr(logging, log_level, None)

        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: %s' % log_level)

        self.logger = logging.getLogger(__name__)
        logging.basicConfig(filename=log_file, encoding="utf-8", level=log_level)

    def log(self, f):
        @wraps(f)
        def logger(*args, **kargs):
            self.logger.info(f'Calling function {f.__name__}')
            try:
                result = f(*args, **kargs) 
                return result
            except Exception as e:
                self.logger.error(f'Function {f.__name__} raised {type(e)}: {e}')
                raise
        return logger

    def profile(self, f):
        @wraps(f)
        def profiler(*args, **kargs):
            start = time.perf_counter()
            result = f(*args, **kargs)
            end = time.perf_counter()
            elapsed_time = end - start
            self.logger.debug(f'Function {f.__name__} ran in {elapsed_time:.6f} seconds')
            return result

        return profiler

    def debug(self, f):
        @wraps(f)
        def debugger(*args, **kargs):
            return f(*args, **kargs)
        return debugger


