from sqlalchemy.exc import SQLAlchemyError
from .db import Session

class AbstractEntity:
    "An abstract class allowing for basic database persistence."

    def save(self):
        #TODO
        pass

    def destroy(self):
        #TODO
        pass



