from user import User
from band import Band
from sqlalchemy import func


def count_user_ids(session):
    return session.query(func.count(User.id)).one()

def return_band_name_and_total_shows_histogram(session):
    bands = session.query(Band).all()
    return {band.name: len(band.shows) for band in bands}


    # band_tuples = session.query(Band.name, Band.shows).all()
    # band_histo = {}
    # for tup in band_tuples:
    #     band_histo[tup[0]] = band.get(band_histo[tup[0]], len(tup[1]))
