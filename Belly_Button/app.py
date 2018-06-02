import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


engine = create_engine("sqlite:///hawaii.sqlite")
base= automap_base()
base.prepare(engine, reflect=True)
mea = base.classes.measurements
sta = base.classes.stations
session = Session(engine)
app = Flask(__name__)

@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Avalable Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end"
    )


@app.route('/api/v1.0/precipitation')
def precipitation():
    lastyear = dt.date.today() - dt.timedelta(days=365)
    precipitation = session.query(mea.date, mea.prcp).filter(mea.date >= lastyear).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
        
@app.route('/api/v1.0/stations')
def stations():
    results = session.query(sta.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    lastyear = dt.date.today() - dt.timedelta(days=365)
    results2 = session.query(mea.station, mea.tobs).filter(mea.date >= lastyear).all()
    tobs = list(np.ravel(results2))
    return jsonify(tobs)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def data(start=None, end=None):
    if not end:
        results = session.query(func.min(mea.tobs), func.avg(mea.tobs), func.max(mea.tobs)).filter(
            mea.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)
    results = session.query(func.min(mea.tobs), func.avg(mea.tobs), func.max(mea.tobs)).filter(
        mea.date >= start).filter(mea.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)


if __name__ == '__main__':
    app.run()
''' /// temps = list(np.ravel(results))
 
@app.route("/api/v1.0/temp/<start>")
     
        
        def stats(start=None, end=None):
        sel = [func.min(measurements.tobs), func.avg(measurements.tobs), func.max()]'''