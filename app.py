# Implementing the get API
from flask import Flask, jsonify

app = Flask(__name__)

Nepal = [{

    "name": "province 1",
    "capital": "biratnagar",
    "CM": "rai",
},

    {

        "name": "province 2",
        "capital": "janakpur",
        "CM": "pandit",
    },

    {

        "name": "province 3",
        "capital": "hetauda",
        "CM": "ppp",
    },

    {

        "name": "province 4",
        "capital": "pokhara",
        "CM": "magar",
    }
    ,
    {

        "name": "province 5",
        "capital": "dang",
        "CM": "pokhrel",
    }
    ,
    {

        "name": "province 6",
        "capital": "surkhet",
        "CM": "shai",
    }

]


@app.route('/')
def index():
    return "welcome to the Nepal API"


@app.route("/Nepal", methods=['GET'])
def get():
    return jsonify({'NP': Nepal})


@app.route("/Nepal", methods=['POST'])
def create():
    next_state = {"name": "province 7",
                  "capital": "dhangadi",
                  "CM": "bhatta"}
    Nepal.append(next_state)
    return jsonify({'created': next_state})



@app.route("/Nepal/<string:CM>",methods=['PUT'])

def state_update(CM):
    Nepal['CM']['name']="Bagmati"
    return jsonify({"new":Nepal[CM]})



@app.route("/Nepal/<CM:string>",methods=['Delete'])
def delete (CM):
    Nepal.remove(Nepal[CM])
    return jsonify({'result':True})



if __name__ == "__main__":
    app.run(debug=True)


