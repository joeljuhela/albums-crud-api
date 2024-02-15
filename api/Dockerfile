FROM python:3.12-bookworm

RUN apt install libmariadb3 libmariadb-dev

WORKDIR /

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./api

ENV PYTHONUNBUFFERED 1

CMD [ "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "api:create_app()" ]