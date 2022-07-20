from flask import Flask
from avtogit.views import detail

app = Flask(__name__)

app.register_blueprint(detail.deteil, url_prefix='/api/v1/detail/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
