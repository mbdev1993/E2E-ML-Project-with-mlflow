FROM python:3.8-slim-buster

RUN apt update && apt install azure-cli -y
WORKDIR /app

COPY . /app/
RUN pip install -r requirements.txt

CMD ["python", "app.py"]