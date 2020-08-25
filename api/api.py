from flask import Blueprint, request, jsonify
from app.selectors import *
import flask
import json
import timeit

bp = Blueprint('api', __name__, url_prefix='/')

@bp.route('/healthz', methods=('GET',))
def health_check():
    start_time = timeit.default_timer()

    # Get the status code and up time
    dataDump = get_health_data()
    status_code = dataDump[0]
    status = ""

    # Set the status according to the code
    if status_code == 200:
        status = "OK"
    elif status_code == 403:
        status = "INVALID"
    elif status_code == 400:
        status = "NOTFOUND"
    else:
        status = "UNKNOWN"

    # Create a object of data (using flask version here as the dummy app version)
    results = {
        'status': status,
        'version': flask.__version__,
        'uptime': "up since " + str(dataDump[1]),
        'execution_time': round(timeit.default_timer() - start_time, 4)
    }
    return json.dumps(results)


