"""Script to seed database."""

import os

import json

from datetime import datetime

import crud

import model

import server


os.system('dropdb web_traffic')

os.system('createdb web_traffic')

model.connect_to_db(server.app)

model.db.create_all()


# Create traffic table's initial data.

with open('data/traffic.json') as f:

    traffic_data = json.loads(f.read())

traffic_in_db = []

for traffic in traffic_data:
    channel_name, from_date, to_date, pull_date, sessions, unique_visitors, direct, google, wix, youtube, bing, n_a, new, returning= (
                                   traffic['channel_name'],
                                   traffic['from_date'],
                                   traffic['to_date'],
                                   traffic['pull_date'],
                                   traffic['sessions'],
                                   traffic['unique_visitors'],
                                   traffic['direct'],
                                   traffic['google'],
                                   traffic['wix'],
                                   traffic['youtube'],
                                   traffic['bing'],
                                   traffic['n_a'],
                                   traffic['new'],
                                   traffic['returning'])

    db_traffic = crud.create_traffic(
                                 channel_name,
                                 from_date,
                                 to_date,
                                 pull_date,
                                 sessions,
                                 unique_visitors,
                                 direct,
                                 google,
                                 wix,
                                 youtube,
                                 bing,
                                 n_a,
                                 new,
                                 returning)

    traffic_in_db.append(db_traffic)

# Create visitor table's initial data.

with open('data/visitor.json') as f:

    visitor_data = json.loads(f.read())

visitor_in_db = []

for visitor in visitor_data:
    channel_name, date, unique_visits= (
                                   visitor['channel_name'],
                                   visitor['date'],
                                   visitor['unique_visits'])

    db_visitor = crud.create_visitor(
                                 channel_name,
                                 date,
                                 unique_visits)

    visitor_in_db.append(db_visitor)
