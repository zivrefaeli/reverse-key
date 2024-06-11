import logging
from datetime import datetime
from typing import Any
from pydantic import BaseModel


class LogFile(BaseModel):
    name: str
    line: int


class LogFormat(BaseModel):
    datetime: datetime
    level: str
    file: LogFile
    message: str
    content: Any


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log = LogFormat(
            datetime=datetime.fromtimestamp(record.created),
            level=record.levelname,
            file=LogFile(
                name=record.filename,
                line=record.lineno,
            ),
            message=record.getMessage(),
            content=record.args,
        )
        return log.model_dump_json()


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler("app.log")
handler.setFormatter(JsonFormatter())
logger.addHandler(handler)
