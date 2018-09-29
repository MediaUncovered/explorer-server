from app import create_app
import config

app = create_app(models_path=config.MODELS_PATH)
app.run(host="0.0.0.0")
