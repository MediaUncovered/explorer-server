from flask import Flask, jsonify, request
from werkzeug.debug import DebuggedApplication
from flask_cors import CORS
import os

from newsAnalysis.Model import Model


def create_app(model_config):
    app = Flask(__name__)
    app.model_config = model_config
    app.model = None

    CORS(app)

    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

    @app.route('/selectModel', methods=['POST'])
    def set_model():
        data = request.get_json()
        app.model = model_config.load_model(data['model_name'])
        return '{}'

    @app.route('/models')
    def index():
        body = model_config.models()
        return jsonify(body)

    @app.route('/query/<string:word>')
    def query(word):
        count = int(request.args.get('count', 50))
        similarWords = app.model.word_embedding.wv.similar_by_word(word, topn=count)
        body = [{"label": result[0], "value": result[1]} for result in similarWords]

        return jsonify(body)

    @app.route('/info')
    def info():
        return app.model.collectionInfo.toJson()

    @app.route('/reliability')
    def reliability():
        body = []
        for elem in app.model.accuracy:
            try:
                percentage = (elem["nr_correct"]/elem["nr_total"]) * 100
            except ZeroDivisionError:
                percentage = 0
            body.append({"section": elem['section'], "nr_total": elem["nr_total"],
                         "nr_correct": elem["nr_correct"], "percentage": round(percentage, 2)})
        return jsonify(body)

    @app.route('/keywordMapping', methods=['POST'])
    def keywordMapping():
        data = request.get_json()
        keywords, oov_kw = app.model.filterNonVocabWords(data['keywords'])
        left_axis, oov_left = app.model.filterNonVocabWords(data['left'])
        right_axis, oov_right = app.model.filterNonVocabWords(data['right'])
        oov = oov_kw + oov_left + oov_right
        if len(right_axis)==0 or len(left_axis)==0:
            mapping = []
        else:
            mapping = app.model.keywordMapping(keywords, left_axis, right_axis).tolist()
        body = {'keywords': keywords, 'mapping': mapping, 'oov': oov}
        return jsonify(body)

    @app.route('/modelInfo')
    def modelInfo():
        return app.model.modelInfo.toJson()

    @app.route('/analogies', methods=['POST'])
    def generateAnalogies():
        data = request.get_json()['wordpair']
        analogies = app.model.generate_analogies(data['a'], data['b'], 3000)
        analogies = analogies[[data['a'], data['b'], 'score']]
        analogies = analogies[analogies['score']>=0.15][:25]
        analogies['score'] = analogies['score'].round(4)
        analogies.rename(columns={data['a']: 'x', data['b']: 'y'},
                         inplace=True)
        return jsonify(analogies.to_dict(orient='records'))

    return app
