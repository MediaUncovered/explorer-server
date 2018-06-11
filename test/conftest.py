import os

import pytest

from app import create_app

@pytest.fixture
def app():
    model_path = os.path.abspath("./models/Moscow_Times_100_fasttext")

    app = create_app(model_path=model_path)
    return app