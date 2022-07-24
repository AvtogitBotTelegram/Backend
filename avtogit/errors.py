class AppError(Exception):
    def __init__(self, reason: str, status: int) -> None:
        super().__init__(f'[{status}] {reason}')
        self.reason = reason
        self.status = status


class NotExcelFileError(AppError):
    status = 409

    def __init__(self, entity: str, descr: str) -> None:
        super().__init__(reason=f'[{entity}] Excel file {descr}', status=self.status)
        self.entity = entity
        self.descr = descr
