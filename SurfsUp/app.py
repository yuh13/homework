from flask import Flask, jsonify


engine - create_engine
base= automap
base.prepare(enginem, reflect=True)
mea = base.classes
sta = base.classes
session = session(engine)
app = FLASK(__name__)

@app.route("/")
def welcome():
    return (
            f'welcome
            f'availbe routes
            f'precip, stations, tobs, tempstart/end
            f'

@app.route('/api/v1.0/preciptition')
def precipitation():
    '''Return the preciipitation data for the last year''''
    #calc the date
    prev_year = date - datetime(-365)
    precip = ses.query prev yrear code
        precip = {date: prcp for date, prcp in precip}
        return jsonify(precip)
        
        
       /// temps = list(np.ravel(results))
 
@app.route("/api/v1.0/temp/<start>")
     
        
        def stats(start=None, end=None):
        sel = [func.min(measurements.tobs), func.avg(measurements.tobs), func.max()]