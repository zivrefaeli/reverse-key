FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY src ./src

ENTRYPOINT [ "uvicorn" ]

CMD [ "main:app", "--app-dir", "src", "--host", "0.0.0.0" ]