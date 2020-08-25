FROM python:3.6.1-alpine
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
RUN apk --no-cache add curl
CMD ["python","manage.py"]