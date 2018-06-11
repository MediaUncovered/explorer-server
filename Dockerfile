FROM python:3.6.5

COPY ./app /flask-explorer/app
COPY ./server.py /flask-explorer/server.py

WORKDIR /flask-explorer

COPY ./requirements.txt /flask-explorer/requirements.txt
RUN pip install -r requirements.txt
COPY ./lib/newsanalysis-0.1.0-py3-none-any.whl /flask-explorer
RUN pip install newsanalysis-0.1.0-py3-none-any.whl

EXPOSE 5000
CMD FLASK_APP=server.py flask run --host 0.0.0.0
