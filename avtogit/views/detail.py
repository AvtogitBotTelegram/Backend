import httpx
import orjson
from flask import Blueprint, request

from avtogit.analyst import Analyst
from avtogit.schemas import ModelDetails

detail = Blueprint('detail', __name__)
orders = Blueprint('orders', __name__)

analyst = Analyst()


@detail.post('/file')
def excel():
    bytes_file = request.files['upload-file'].read()
    bad_details = analyst.expired_details(bytes_file)
    return orjson.dumps([ModelDetails.from_orm(entity).dict() for entity in bad_details])


@detail.post('/url')
def url():
    url_file = request.json['url']
    bytes_file = httpx.get(url_file).content
    bad_details = analyst.expired_details(bytes_file)
    return orjson.dumps([ModelDetails.from_orm(entity).dict() for entity in bad_details])


@orders.post('/')
def send_orders():
    orders = orjson.loads(request.data)
    return ('True', 200)
