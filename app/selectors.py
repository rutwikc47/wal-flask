import flask
import time
import requests
import psutil

def get_health_data():
    req = requests.get('http://localhost:8080/')
    status_code = req.status_code

    from manage import startTime
    currTime = startTime

    cpuUsage = psutil.cpu_percent()
    memoryUsage = psutil.virtual_memory().percent

    return([status_code, currTime, cpuUsage, memoryUsage])
