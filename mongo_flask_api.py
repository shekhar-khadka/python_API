from flask import Flask
from flask_pymongo import PyMongo

from bson.json_util import dumps


from flask import jsonify, request

app = Flask(__name__)

app.secret_key="security"
app.config['MONGO_URI']='mongodb://localhost:27017/flight'

mongo = PyMongo(app)

@app.route('/add',methods=['POST'])
def add_flight():
    _json=request.json
    _flight_number = _json['flight_number']
    _airlines_name= _json['airlines_name']
    _source= _json['source']
    _destination=_json['destination']
    _duration=_json['duration']



    #_hashed_password=generate_password_hash(_number)
    mongo.db.flight_data.insert({'airlines_name':_airlines_name,
                                 'flight_number':_flight_number,
                                        'source':_source,
                                        'destination':_destination,
                                        'duration':_duration
                                 })

    resp=jsonify('added successfully')
    resp.status_code=200
    return resp


@app.route('/find',methods=['GET'])

def get_flight_status():
    status=mongo.db.flight_data.find()
    resp=dumps(status)
    return resp

#get flight by flight_number

@app.route('/find/<number>',methods=['GET'])

def get_flight_by_number(number):
    status=mongo.db.flight_data.find({'flight_number':number})
    resp=dumps(status)
    return resp

@app.route('/delete/<number>',methods=['DELETE'])

def delete_flight_by_number(number):
    mongo.db.flight_data.delete_one({'flight_number':number})
    resp=jsonify("flight deleted")
    resp.status_code=200
    return resp


#changing the flight number which matches the flight_time
@app.route('/update/<flight_time>',methods=['PUT'])

def update_flight(flight_time):
    _json=request.json
    _flight_number = _json['flight_number']

    mongo.db.flight_data.update_one({"duration":flight_time},{"$set":{"flight_number":_flight_number}})
    resp=jsonify("flight updated")
    resp.status_code=200
    return resp

if __name__ == "__main__":
    app.run(debug=True)



