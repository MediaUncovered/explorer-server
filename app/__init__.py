from flask import Flask, jsonify, request
from flask_cors import CORS
import os

from newsAnalysis.Model import Model


def create_app(model_config):
    app = Flask(__name__)
    app.model_config = model_config
    app.model = None

    CORS(app)

    def get_model(model_name):
        return model_config.load_model(model_name)

    @app.route('/models')
    def index():
        body = model_config.models()
        return jsonify(body)

    @app.route('/models/<string:model_name>/query/<string:word>')
    def query(model_name, word):
        count = int(request.args.get('count', 30))

        similarWords = get_model(model_name).word_embedding.wv.similar_by_word(word, topn=count)
        body = [{"label": result[0], "value": result[1]} for result in similarWords]

        return jsonify(body)

    @app.route('/models/<string:model_name>/info')
    def info(model_name):
        return get_model(model_name).collectionInfo.toJson()

    @app.route('/models/<string:model_name>/reliability')
    def reliability(model_name):
        body = [{"section": elem['section'], "nr_total": elem["nr_total"], "nr_correct": elem["nr_correct"]} for elem in get_model(model_name).accuracy]
        return jsonify(body)

    @app.route('/models/<string:model_name>/keywordMapping', methods=['POST'])
    def keywordMapping(model_name):
        data = request.get_json()
        mapping = get_model(model_name).keywordMapping(data['keywords'], data['left'], data['right'])
        body = {'mapping': list(mapping)}
        return jsonify(body)

    @app.route('/models/<string:model_name>/modelInfo')
    def modelInfo(model_name):
        return get_model(model_name).modelInfo.toJson()

    @app.route('/analogies', methods=['POST'])
    def generateAnalogies(model_name):
        data = [{'x':'x', 'y':'y', 'score':0.75}, {'x':'x2', 'y':'y2', 'score':0.33}]
        return jsonify(data)

    return app
