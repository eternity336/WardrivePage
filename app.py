from flask import Flask, render_template, jsonify
from flask import request
import bluetooth_discover as bd
import essid_discover as ed

app = Flask(__name__)

@app.route("/")
def home():
    ## Homepage for Monitor 
    return render_template('index.html')

@app.route("/getdata")
def get_data():
    ## Data that is refreshed every sec to homepage
    data = {
        'ed':ed.get_devices(), 
        'bd':bd.get_devices(), 
        }
    message = {
            'status' : 200,
            'message' : 'OK',
            'data' : data
            }
    resp = jsonify(message)
    return resp