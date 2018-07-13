from base import *

class UserShow(Base):
    __tablename__ = "user_shows"
    user_id = Column(INTEGER, ForeignKey("users.id"), primary_key=True)
    show_id = Column(INTEGER, ForeignKey("shows.id"), primary_key=True)
