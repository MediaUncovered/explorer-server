Explorer-Flask
==============

Backend to display media uncovered files


Building
--------
`docker build -t media-uncovered/explorer-server:dev .`


Development
-----------
After you've built your image use
`docker-compose up`
to start a development server on port 5000. Any changes made under ./src and ./models
will be reflected in the running application.


Models
------
Are created by using the NewsAnalysis project. See https://github.com/MediaUncovered/NewsAnalysis for details.


