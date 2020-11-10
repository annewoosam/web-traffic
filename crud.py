"""CRUD operations."""

from model import db, Traffic, Visitor, connect_to_db

import datetime


def create_traffic(channel_name, from_date, to_date, pull_date, sessions, unique_visitors, direct, google, wix, youtube, bing, n_a, new, returning):
   

    traffic = Traffic(channel_name=channel_name,
                  from_date=from_date,
                  to_date=to_date,
                  pull_date=pull_date,
                  sessions=sessions,
                  unique_visitors=unique_visitors,
                  direct=direct,
                  google=google,
                  wix=wix,
                  youtube=youtube,
                  bing=bing,
                  n_a=n_a,
                  new=new,
                  returning=returning)

    db.session.add(traffic)

    db.session.commit()

    return traffic

def get_traffic():
    """Return all rows of traffic data."""

    return Traffic.query.all()

def create_visitor(channel_name, date, unique_visits):
   

    visitor = Visitor(channel_name=channel_name,
                  date=date,
                  unique_visits=unique_visits)

    db.session.add(visitor)

    db.session.commit()

    return visitor

def get_visitors():
    """Return all rows of visitor data."""

    return Visitor.query.all()
 
if __name__ == '__main__':
    from server import app
    connect_to_db(app)
