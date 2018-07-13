from base import *

class Band(Base):
    __tablename__ = "bands"
    id = Column(INTEGER, primary_key = True)
    name = Column(TEXT)
    shows = relationship("Show", back_populates = "band")
    songs = relationship("Song", back_populates = "band")
