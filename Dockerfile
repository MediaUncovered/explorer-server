FROM python:3.6.5

COPY ./src /flask-explorer
COPY ./requirements.txt /flask-explorer/requirements.txt

WORKDIR /flask-explorer
RUN pip install -r requirements.txt

EXPOSE 5000
CMD FLASK_APP=server.py flask run --host 0.0.0.0
