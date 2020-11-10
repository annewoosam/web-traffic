"""Server for YourFolder app."""

# increased flask

from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# created import allowing connection to database

from model import connect_to_db, YourModelNameTitleCaseSingularStats, db

app = Flask(__name__)

# imported Jinja secret key settings
from jinja2 import StrictUndefined

app.secret_key = "dev"

app.jinja_env.undefined = StrictUndefined

import crud

@app.route('/')

def all_traffic():

    stats=crud.get_traffic()
    
    channel_id=[q[0] for q in db.session.query(Traffic.channel_id).all()]

    channel_name=[q[0] for q in db.session.query(Traffic.channel_name).all()]
     
    from_date=[q[0] for q in db.session.query(Traffic.from_date).all()]

    to_date=[q[0] for q in db.session.query(Traffic.to_date).all()]

    pull_date=[q[0] for q in db.session.query(Traffic.pull_date).all()]

    sessions=[q[0] for q in db.session.query(Traffic.sessions).all()]

    unique_visitors=[q[0] for q in db.session.query(Traffic.unique_visitors).all()]

    direct=[q[0] for q in db.session.query(Traffic.direct).all()]

    google=[q[0] for q in db.session.query(Traffic.google).all()]

    wix=[q[0] for q in db.session.query(Traffic.wix).all()]

    youtube=[q[0] for q in db.session.query(Traffic.youtube).all()]

    bing=[q[0] for q in db.session.query(Traffic.bing).all()]

    n_a=[q[0] for q in db.session.query(YourModelNameInTitleCaseHere.n_a).all()]

    new=[q[0] for q in db.session.query(YourModelNameInTitleCaseHere.new).all()]
  
    returning=[q[0] for q in db.session.query(YourModelNameInTitleCaseHere.returning).all()]
    
    stats=crud.get_visitors()
    
    visitor_id=[q[0] for q in db.session.query(Visitors.visitor_id).all()]
      
    date=[q[0] for q in db.session.query(Visitors.date).all()]

    unique_visit=[q[0] for q in db.session.query(Visitors.unique_visit).all()]

    return render_template('traffic.html', channel_id=channel_id, channel_name=channel_name, from_date=from_date, to_date=to_date, pull_date+pull_date, sessions=sessions, unique_visitors=unique_visitors, direct=direct,google=google,wix=wix,youtube=youtube,bing=bing, n_a=n_a, new=new, returning=returning, visitor_id=visitor_id, date=date, unique_visit=unique_visit)

if __name__ == '__main__':

# added connection to database

    connect_to_db(app)

# during development

    app.run(host='0.0.0.0', debug=True)

# in production

    #app.run()