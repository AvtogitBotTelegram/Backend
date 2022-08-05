from flask import Flask

from avtogit.errors import AppError
from avtogit.views import detail


def handle_app_errors(error: AppError):
    return {'error': error.reason}, error.status


app = Flask(__name__)

app.register_blueprint(detail.detail, url_prefix='/api/v1/detail/upload')
app.register_blueprint(detail.orders, url_prefix='/api/v1/orders/upload')

app.register_error_handler(AppError, handle_app_errors)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
