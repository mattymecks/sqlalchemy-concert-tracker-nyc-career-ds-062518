from base import *

class Song(Base):
    __tablename__ = "songs"
    id = Column(INTEGER, primary_key = True)
    name = Column(TEXT)
    band_id = Column(INTEGER, ForeignKey("bands.id"))
    band = relationship("Band", back_populates = "songs")
    shows = relationship("Show", secondary = "show_songs", back_populates = "songs")
