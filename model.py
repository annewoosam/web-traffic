from flask_sqlalchemy import SQLAlchemy

import datetime

db = SQLAlchemy()

class Traffic(db.Model):
    """A class for traffic ."""
    
    __tablename__ = 'traffic'

    traffic_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    channel_name = db.Column(db.String)

    from_date = db.Column(db.Date)

    to_date = db.column(db.Date)

    pull_date = db.column(db.Date)

    sessions = db.Column(db.Integer)

    unique_visitors = db.Column(db.Integer)

    direct = db.Column(db.Integer)

    google = db.Column(db.Integer)
    
    wix = db.Column(db.Integer)

    youtube = db.Column(db.Integer)

    bing = db.Column(db.Integer)

    n_a = db.Column(db.Integer)

    new = db.Column(db.Integer)

    returning = db.Column(db.Integer)

    def __repr__(self):
        return f'<Traffic traffic_id={self.traffic_id} channel_name={self.channel_name}>'

class Visitor(db.Model):
    """A class for visitor ."""
    
    __tablename__ = 'visitors'

    visitor_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    channel_name = db.Column(db.String)

    date = db.Column(db.Date)

    unique_visits = db.Column(db.Integer)

# keep repeating till all column names finished

    def __repr__(self):
        return f'<Visitor visitor_id={self.visitor_id} channel_name={self.channel_name}>'

def connect_to_db(flask_app, db_uri='postgresql:///web_traffic', echo=True):
   
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
   
    flask_app.config['SQLALCHEMY_ECHO'] = echo
   
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':

    from server import app

    connect_to_db(app)