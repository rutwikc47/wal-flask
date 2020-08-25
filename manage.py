import os
from app import create_app
import datetime

now = datetime.datetime.now()

application = create_app()

if __name__ == '__main__':
    application.run(host="localhost", port=8080, debug=True)

startTime = now.strftime('%Y-%m-%d %H:%M:%S')
