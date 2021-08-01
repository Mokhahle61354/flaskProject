from flask import Flask
from .endpoint.pages import compare_city

app = Flask(__name__)
app.register_blueprint(compare_city)

if __name__ == '__main__':
    app.run()
