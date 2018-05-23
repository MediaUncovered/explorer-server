Explorer-Flask
==============

Backend to display media uncovered files

Building
--------
`docker build -t media-uncovered/explorer-flask:dev .`

Development
-----------

After you've built your image use
`docker run -v <PATH_TO_PROJECT_FILES>/src:/flask-explorer -p 5000:5000 -t media-uncovered/explorer-flask:dev`
to start a development server on port 5000. Any changes made under ./src
will be reflected in the running application.
