import logging
# import threading
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from config import settings


logger = logging.getLogger(__name__)
Base = declarative_base()
engine = create_engine(settings.database_url)
Session = scoped_session(sessionmaker(bind=engine))
# lock = threading.Lock()


@contextmanager
def session_scope():
    session = Session()
    # session.expire_on_commit = False
    try:
        # lock.acquire()
        yield session
        session.commit()
    except Exception as e:
        logger.error(f'action=session_scope error={e}')
        session.rollback()
        raise
    finally:
        # session.expire_on_commit = True
        session.close()
        # lock.release()


def init_db():
    import models
    Base.metadata.create_all(bind=engine)
