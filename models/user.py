from base import *
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(INTEGER, primary_key = True)
    name = Column(TEXT)
    shows = relationship("Show", secondary = "user_shows", back_populates = "users")

    def total_shows(self):
        return len(self.shows)

    def first_show(self):
        show_dict = {show : show.date for show in self.shows}
        earliest_show = min(show_dict.items(), key=lambda x: x[1])[0]
        earliest_date = earliest_show.date.strftime('%m/%d/%Y')

        # earliest_date = min(show_dict, key=show_dict.get)
        # earliest_show = k for k,v in show_dict if v = earliest_date

        # for item in show_dict:
        #     earliest_show = None
        #     earliest_date = 07/12/2900
        #     for show, date in item.items():
        #         if show < earliest_date:
        #             earliest_show = show
        #             earliest_date = date
        #     return earliest_date
        #
        # first_show_obj = session.query(Show).filter(Show.id = earliest_date).first()

        return earliest_show.band.name + " - " + earliest_date + " - " + earliest_show.venue.name + ", " + earliest_show.venue.city.name

    #'Band Name - MM/DD/YYYY - Venue Name, City Name'


# import datetime
# object.attribute.strftime(%m,%d,%Y)
