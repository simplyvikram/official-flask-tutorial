
from sqlalchemy import Column, Integer, String
import database

class Entry(database.Base):

    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True)
    mssg = Column(String(200), unique=True)

    def __init__(self, title=None, mssg=None):
        self.title = title
        self.mssg = mssg

    def __repr__(self):
        return '<Entry> %s - %s - %s' % (self.id, self.title, self.mssg)