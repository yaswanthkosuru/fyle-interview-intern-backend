FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7755


VOLUME /sqlite


CMD ["bash", "run.sh"]

