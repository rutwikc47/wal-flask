import flask
import time
import requests

def get_health_data():
    req = requests.get('http://localhost:8080/')
    status_code = req.status_code

    from manage import startTime
    currTime = startTime

    return([status_code, currTime])
