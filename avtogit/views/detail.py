from flask import Blueprint, request


detail = Blueprint('detail', __name__)


@detail.post('/excel')
def excel():
    file = request.files['upload-file'].read()
    return 'true'
