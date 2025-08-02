from functools import wraps
import logging
import time

logger = logging.getLogger('utilidec_logger')
logging.basicConfig(filename='utilidec.log', encoding="utf-8", level='DEBUG')

def log(f):
    @wraps(f)
    def wrapper(*args, **kargs):
        logger.info(f'Calling function {f.__name__}')
        try:
            result = f(*args, **kargs) 
            return result
        except Exception as e:
            logger.error(f'Function {f.__name__} raised {type(e)}: {e}')
            raise
    return wrapper

def profile(f):
    @wraps(f)
    def wrapper(*args, **kargs):
        start = time.perf_counter()
        result = f(*args, **kargs)
        end = time.perf_counter()
        elapsed_time = end - start
        logger.info(f'Function {f.__name__} ran in {elapsed_time:.6f} seconds')
        return result
    return wrapper
