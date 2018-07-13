from base import *

class City(Base):
    __tablename__ = "cities"
    id = Column(INTEGER, primary_key = True)
    name = Column(TEXT)
    venues = relationship("Venue", back_populates = "city")
