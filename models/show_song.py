from base import *


class ShowSong(Base):
    __tablename__ = "show_songs"
    id = Column(INTEGER, primary_key = True)
    length = Column(INTEGER)
    notes = Column(TEXT)
    show_id = Column(INTEGER, ForeignKey("shows.id"))
    song_id = Column(INTEGER, ForeignKey("songs.id"))
    show = relationship("Show", backref=backref("show_songs", cascade="all, delete-orphan"))
    song = relationship("Song", backref=backref("show_songs", cascade="all, delete-orphan"))
