import os

import yaml

from newsAnalysis.Model import Model


class ModelConfig(object):

    _models_path = None
    _models = None

    def models(self):
        # models = [model for model in self._models]
        return list(self._models.keys())

    def load_model(self, model_name):
        model_file_name = self._models[model_name]["file"]
        model_path = os.path.join(self._models_path, model_file_name)
        model = Model().load(model_path=model_path)
        return model


MODELS_PATH = os.getenv('MODELS_PATH', './models')
MODELS_CONFIG_PATH = os.getenv('MODELS_CONFIG_PATH', os.path.join(MODELS_PATH, "config.yml"))


def load_model_config():
    stream = open(MODELS_CONFIG_PATH, "r")
    models_raw = yaml.load_all(stream)
    models = [model for model in models_raw]

    model_config = ModelConfig()
    model_config._models = models[0]
    model_config._models_path = MODELS_PATH

    return model_config


model_config = load_model_config()