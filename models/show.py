from base import *


class Show(Base):
    __tablename__ = "shows"
    id = Column(INTEGER, primary_key = True)
    date = Column(DATE)
    band_id = Column(INTEGER, ForeignKey("bands.id"))
    venue_id = Column(INTEGER, ForeignKey("venues.id"))
    band = relationship("Band", back_populates = "shows")
    venue = relationship("Venue", back_populates = "shows")
    users = relationship("User", secondary = "user_shows", back_populates = "shows")
    songs = relationship("Song", secondary = "show_songs", back_populates = "shows")
