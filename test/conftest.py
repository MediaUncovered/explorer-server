import os

import pytest

from app import create_app

@pytest.fixture
def app():
    models_path = os.path.abspath("./test/models")

    app = create_app(models_path=models_path)
    return app