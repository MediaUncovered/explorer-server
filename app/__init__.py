import os
import json

from flask import Flask, jsonify, request
from flask_cors import CORS

from newsAnalysis.Model import Model
import config


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.model = Model().load(model_path=config.MODEL_PATH)


    @app.route('/query/<string:word>')
    def query(word):
        count = int(request.args.get('count', 30))

        similarWords = app.model.word_embedding.wv.similar_by_word(word, topn=count)
        body = [{"label": result[0], "value": result[1]} for result in similarWords]

        return jsonify(body)

    @app.route('/info')
    def info():
        return app.model.collectionInfo.toJson()

    @app.route('/reliability')
    def reliability():
        body = [{"section": elem['section'], "nr_total": elem["nr_total"], "nr_correct": elem["nr_correct"]} for elem in app.model.accuracy]
        return jsonify(body)

    @app.route('/keywordMapping', methods=['POST'])
    def keywordMapping():
        data = request.get_json()
        mapping = app.model.keywordMapping(data['keywords'], data['left'], data['right'])
        body = {'mapping': list(mapping)}
        return jsonify(body)

    @app.route('/modelInfo')
    def modelInfo():
        return app.model.modelInfo.toJson()

    @app.route('/analogies', methods=['POST'])
    def generateAnalogies():
        data = [{'x':'x', 'y':'y', 'score':0.75}, {'x':'x2', 'y':'y2', 'score':0.33}]
        return jsonify(data)

    return app
