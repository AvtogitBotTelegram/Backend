from datetime import datetime, timedelta

import pandas

from avtogit.schemas import ModelDetails
from avtogit.errors import NotExcelFileError


class Analyst:

    def expired_details(self, bytes_file: bytes) -> list[ModelDetails]:
        try:
            file = pandas.read_excel(bytes_file)
        except ValueError:
            raise NotExcelFileError('file', 'reason: Not found excel file')

        file['Ожидаемый срок'] = pandas.to_datetime(file['Ожидаемый срок'], format='%d.%m.%Y %H:%M')
        details = file[
            (file['Готово к выдаче, шт'].notna()) &
            ((file['Ожидаемый срок'] + timedelta(days=15)) < datetime.now()) &
            (file['Цена в закупке, ₽'] > 1000)
        ]
        bad_details = []
        for detail in details.itertuples():
            bad_details.append(
                ModelDetails(
                    customer_name=detail[5],
                    detail_number=detail[7],
                    detail_name=detail[8],
                    detail_price=detail[14],
                    expected_time=detail[20].to_pydatetime(),
                )
            )
        return [ModelDetails.from_orm(detail) for detail in bad_details]
