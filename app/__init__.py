from flask import Flask, jsonify, request
from flask_cors import CORS
import os

from newsAnalysis.Model import Model


def create_app(model_config):
    app = Flask(__name__)
    app.model_config = model_config
    app.model = None

    CORS(app)

    @app.route('/models/<string:model_name>')
    def set_model(model_name):
        app.model = model_config.load_model(model_name)
        return '{}'

    @app.route('/models')
    def index():
        body = model_config.models()
        return jsonify(body)

    @app.route('/models/query/<string:word>')
    def query(word):
        count = int(request.args.get('count', 30))
        similarWords = app.model.word_embedding.wv.similar_by_word(word, topn=count)
        body = [{"label": result[0], "value": result[1]} for result in similarWords]

        return jsonify(body)

    @app.route('/models/info')
    def info():
        return app.model.collectionInfo.toJson()

    @app.route('/models/reliability')
    def reliability():
        body = [{"section": elem['section'], "nr_total": elem["nr_total"], "nr_correct": elem["nr_correct"]} for elem in app.model.accuracy]
        return jsonify(body)

    @app.route('/models/keywordMapping', methods=['POST'])
    def keywordMapping():
        data = request.get_json()
        mapping = app.model.keywordMapping(data['keywords'], data['left'], data['right'])
        body = {'mapping': list(mapping)}
        return jsonify(body)

    @app.route('/models/modelInfo')
    def modelInfo():
        return app.model.modelInfo.toJson()

    @app.route('/analogies', methods=['POST'])
    def generateAnalogies():
        data = [{'x':'x', 'y':'y', 'score':0.75}, {'x':'x2', 'y':'y2', 'score':0.33}]
        return jsonify(data)

    return app
