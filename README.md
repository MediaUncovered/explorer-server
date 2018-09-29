Explorer-Flask
==============

Backend to display media uncovered files


Building
--------
`docker build -t media-uncovered/explorer-server:dev .`


Development
-----------
After you've built your image use
`docker run -v <PATH_TO_PROJECT_FILES>/app:/flask-explorer/app -v <PATH_TO_PROJECT_FILES>/models:/flask-explorer/models -e MODEL_PATH=./models/model -p 5000:5000 -t media-uncovered/explorer-server:dev`
to start a development server on port 5000. Any changes made under ./src
will be reflected in the running application.


Models
------
Are created by using the NewsAnalysis project. See https://github.com/MediaUncovered/NewsAnalysis for details.


