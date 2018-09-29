import os

import yaml

from newsAnalysis.Model import Model


class ModelConfig(object):

    _models_path = None
    _models = None

    def models(self):
        models = [model["label"] for model in self._models]
        return models

    def load_model(self, model_name):
        model_path = os.path.join(self._models_path, model_name)
        model = Model().load(model_path=model_path)
        return model


MODELS_PATH = os.getenv('MODELS_PATH', './models')
MODELS_CONFIG_PATH = os.getenv('MODELS_CONFIG_PATH', os.path.join(MODELS_PATH, "config.yml"))


def load_model_config():
    stream = open(MODELS_CONFIG_PATH, "r")
    models = yaml.load_all(stream)

    model_config = ModelConfig()
    model_config._models = models
    model_config._models_path = MODELS_PATH

    return model_config


model_config = load_model_config()