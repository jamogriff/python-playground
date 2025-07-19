from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///jamobank.db', future=True, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
