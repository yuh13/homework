import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify, render_template, request, redirect

#############
# Flask Setup
#############

#############
# Data Setup
#############
from flask_sqlalchemy import SQLAlchemy

engine = create_engine("sqlite:///belly_button_biodiversity.sqlite")
base= automap_base()
base.prepare(engine, reflect=True)
inspector = inspect(engine)
bacteria_table = base.classes.bacteria
otu_table = base.classes.otu
samples_table = base.classes.samples
samples_metadata_table = base.classes.samples_metadata
session = Session(engine)


app = Flask(__name__)

@app.route("/")
def home():
    """ Render Home Page"""
    return render_template("index.html")

@app.route("/names")
def names():
    """ Return List of names """
    sample_names = []
    columns = inspector.get_columns("samples")
    for column in columns:
        sample_names.append(column["name"])
    sample_names = sample_names[1:]
    return jsonify(sample_names)

@app.route("/otu")    
def otu_list():
    """List of OTU descriptions"""
    otu_description = session.query(otu_table.lowest_taxonomic_unit_found).all()
    return jsonify(otu_description)

@app.route("/metadata/<sample>")
def metadata(sample):
    """MetaData for a given sample"""
    results = session.query(samples_metadata_table.AGE, samples_metadata_table.BBTYPE, samples_metadata_table.ETHNICITY, samples_metadata_table.GENDER, samples_metadata_table.LOCATION, samples_metadata_table.SAMPLEID
        ).filter(
            samples_metadata_table.SAMPLEID == sample.split("_")[1]).all()
    df = pd.DataFrame(results, columns = ['AGE', 'BBTYPE', 'ETHNICITY', 'GENDER', 'LOCATION','SAMPLEID'])
    df['AGE'] = df['AGE'].astype(float)
    return jsonify(df.to_dict(orient="records"))

@app.route("/wfreq/<sample>")
def washfreq(sample):
    """Weekly Washing Frequency as a number"""
    results = session.query(samples_metadata_table.WFREQ).filter(           samples_metadata_table.SAMPLEID == sample.split("_")[1]).all()
    return jsonify(results[0])

@app.route("/samples/<sample>")
def samples_count(sample):
    """OTU IDs and counts for a given sample"""
    search = getattr(samples_table, sample)
    results = session.query(search).all()
    df = pd.DataFrame(results).sort_values(sample, ascending=False)
    df[sample]
    df[sample] = df[sample].astype(float)
    df = df.reset_index(inplace=False)
    df = df.rename(columns={"index":"otu_ids"})
    results = [{"otu_ids": df["otu_ids"].tolist(), "sample_values": df[sample].tolist()}]
    return jsonify(results)

#@app.route("/api/v1.0/temp/<start>")
#@app.route("/api/v1.0/temp/<start>/<end>")
#def data(start=None, end=None):
#    if not end:
#        results = session.query(func.min(mea.tobs), func.avg(mea.tobs), func.max(mea.tobs)).filter(
#            mea.date >= start).all()
#        temps = list(np.ravel(results))
#        return jsonify(temps)
#    results = session.query(func.min(mea.tobs), func.avg(mea.tobs), func.max(mea.tobs)).filter(
#        mea.date >= start).filter(mea.date <= end).all()
#    temps = list(np.ravel(results))
#    return jsonify(temps)

#@app.route("")
if __name__ == '__main__':
    app.run(debug=True)

    
    
    
    
#########
# Trial Code
########
    
 #app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///belly_button_biodiversity.sqlite"
#
#db = SQLAlchemy(app)
#
#class Bacteria(db.Model):
#    __tablename__ = "bacteria"
#    
#    id = db.Column(db.Integer, primary_key = True)
#    event = db.Column(db.String)
#    ethnicity = db.Column(db.String)
#    gender = db.Column(db.String)
#    age = db.Column(db.Integer)
#    wfreq = db.Column(db.Integer)
#    bbtype = db.Column(db.String)
#    location = db.Column(db.String)
#    country012 = db.Column(db.String)
#    zip012 = db.Column(db.Integer)
#    country1319 = db.Column(db.String)
#    zip1319 = db.Column(db.Integer)
#    dog = db.Column(db.String)
#    cat = db.Column(db.String)
#    impsurface013 = db.Column(db.Integer)
#    npp013 = db.Column(db.Float)
#    mmaxtemp013 = db.Column(db.Float)
#    pfc013 = db.Column(db.Float)
#    impsurface1319 = db.Column(db.Integer)
#    npp1319 = db.Column(db.Float)
#    mmaxtemp1319 = db.Column(db.Float)
#    pfc1319 = db.Column(db.Float)
#    
#    def __repr__(self):
#        return '<Event %r>' % self.event
  
    
    
    
    
########### 
# Surfs Up Code
##########

#@app.route("/")
#def welcome():
#    return (
#        f"Welcome to the Hawaii Climate Analysis API!<br/>"
#        f"Avalable Routes:<br/>"
#        f"/api/v1.0/precipitation<br/>"
#        f"/api/v1.0/stations<br/>"
#        f"/api/v1.0/tobs<br/>"
#        f"/api/v1.0/temp/start/end"
#    )

#
#@app.route('/api/v1.0/precipitation')
#def precipitation():
#    lastyear = dt.date.today() - dt.timedelta(days=365)
#    precipitation = session.query(mea.date, mea.prcp).filter(mea.date >= lastyear).all()
#    precip = {date: prcp for date, prcp in precipitation}
#    return jsonify(precip)
#        
#@app.route('/api/v1.0/stations')
#def stations():
#    results = session.query(sta.station).all()
#    stations = list(np.ravel(results))
#    return jsonify(stations)
#
#@app.route("/api/v1.0/tobs")
#def tobs():
#    lastyear = dt.date.today() - dt.timedelta(days=365)
#    results2 = session.query(mea.station, mea.tobs).filter(mea.date >= lastyear).all()
#    tobs = list(np.ravel(results2))
#    return jsonify(tobs)
#
#@app.route("/api/v1.0/temp/<start>")
#@app.route("/api/v1.0/temp/<start>/<end>")
#def data(start=None, end=None):
#    if not end:
#        results = session.query(func.min(mea.tobs), func.avg(mea.tobs), func.max(mea.tobs)).filter(
#            mea.date >= start).all()
#        temps = list(np.ravel(results))
#        return jsonify(temps)
#    results = session.query(func.min(mea.tobs), func.avg(mea.tobs), func.max(mea.tobs)).filter(
#        mea.date >= start).filter(mea.date <= end).all()
#    temps = list(np.ravel(results))
#    return jsonify(temps)
