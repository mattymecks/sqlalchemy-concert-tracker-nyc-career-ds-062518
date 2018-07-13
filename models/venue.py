from base import *

class Venue(Base):
    __tablename__ = "venues"
    id = Column(INTEGER, primary_key = True)
    name = Column(TEXT)
    capacity = Column(INTEGER)
    city_id = Column(INTEGER, ForeignKey("cities.id"))
    shows = relationship("Show", back_populates = "venue")
    city = relationship("City", back_populates = "venues")
