import orjson
from flask import Blueprint, request

from avtogit.analyst import Analyst
from avtogit.schemas import ModelDetails

detail = Blueprint('detail', __name__)

analyst = Analyst()


@detail.post('/expired-details')
def excel():
    bytes_file = request.files['upload-file'].read()
    bad_details = analyst.expired_details(bytes_file)
    return orjson.dumps([ModelDetails.from_orm(entity).dict() for entity in bad_details])
