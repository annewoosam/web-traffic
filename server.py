"""Server for Web-Traffic app."""

# increased flask

from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# created import allowing connection to database

from model import connect_to_db, Traffic, Visitor, db

app = Flask(__name__)

# imported Jinja secret key settings
from jinja2 import StrictUndefined

app.secret_key = "dev"

app.jinja_env.undefined = StrictUndefined

import crud

@app.route('/')

def all_traffic():

    stats=crud.get_traffic()

    stats2=crud.get_visitors()
    
    traffic_id=[q[0] for q in db.session.query(Traffic.traffic_id).all()]

    channel_name=[q[0] for q in db.session.query(Traffic.channel_name).all()]
     
    from_date=[q[0] for q in db.session.query(Traffic.from_date).all()]

    #to_date=[q[0] for q in db.session.query(Traffic.to_date).all()]

    # pull_date=[q[0] for q in db.session.query(Traffic.pull_date).all()]

    sessions=[q[0] for q in db.session.query(Traffic.sessions).all()]

    unique_visitors=[q[0] for q in db.session.query(Traffic.unique_visitors).all()]

    direct=[q[0] for q in db.session.query(Traffic.direct).all()]

    google=[q[0] for q in db.session.query(Traffic.google).all()]

    wix=[q[0] for q in db.session.query(Traffic.wix).all()]

    youtube=[q[0] for q in db.session.query(Traffic.youtube).all()]

    bing=[q[0] for q in db.session.query(Traffic.bing).all()]

    n_a=[q[0] for q in db.session.query(Traffic.n_a).all()]

    new=[q[0] for q in db.session.query(Traffic.new).all()]
  
    returning=[q[0] for q in db.session.query(Traffic.returning).all()]
    
    visitor_id=[q[0] for q in db.session.query(Visitor.visitor_id).all()]
      
    date=[q[0] for q in db.session.query(Visitor.date).all()]

    unique_visits=[q[0] for q in db.session.query(Visitor.unique_visits).all()]

    return render_template('traffic.html', stats=stats, stats2=stats2,traffic_id=traffic_id,
     channel_name=channel_name, from_date=from_date, sessions=sessions,
     unique_visitors=unique_visitors, direct=direct, google=google, wix=wix, youtube=youtube, bing=bing, n_a=n_a,
     new=new, returning=returning, visitor_id=visitor_id, date=date, unique_visits=unique_visits)

if __name__ == '__main__':

# added connection to database

    connect_to_db(app)

# during development

    app.run(host='0.0.0.0', debug=True)

# in production

    #app.run()