import os

from flask import Flask, jsonify, request
from flask_cors import CORS

from newsAnalysis.Model import Model


def create_app(model_path=None):
    app = Flask(__name__)
    CORS(app)

    if model_path is None:
        model_path = os.path.abspath("./models/model")
        model_path = '../NewsAnalysis/models/Moscow_Times_1000_fasttext'

    app.model = Model().load(model_path=model_path)

    @app.route('/query/<string:word>')
    def query(word):
        count = int(request.args.get('count', 10))

        similarWords = app.model.word_embedding.wv.similar_by_word(word, topn=count)
        body = [{"label": result[0], "value": result[1]} for result in similarWords]

        return jsonify(body)

    @app.route('/info')
    def info():
        return app.model.collectionInfo.toJson()

    @app.route('/keywordMapping', methods=['POST'])
    def keywordMapping():
        data = request.get_json()
        mapping = app.model.keywordMapping(data['keywords'], data['left'], data['right'])
        body = {'mapping': list(mapping)}
        return jsonify(body)

    return app
