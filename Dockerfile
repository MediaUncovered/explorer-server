FROM python:3.6.5

COPY ./app /flask-explorer/app
COPY ./requirements.txt /flask-explorer/requirements.txt
COPY ./server.py /flask-explorer/server.py

WORKDIR /flask-explorer
RUN pip install -r requirements.txt

EXPOSE 5000
CMD FLASK_APP=server.py flask run --host 0.0.0.0
