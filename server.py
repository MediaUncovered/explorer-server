from app import create_app, config

app = create_app(model_config=config.model_config)
app.run(host="0.0.0.0")
