FROM python:3.11-slim

WORKDIR /app

COPY requriremnets.txt ./

RUN pip install -r requriremnets.txt

COPY src ./src

ENTRYPOINT [ "uvicorn" ]

CMD [ "main:app", "--app-dir", "src", "--host", "0.0.0.0" ]