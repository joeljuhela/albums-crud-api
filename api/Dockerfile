FROM python:3.12-bookworm

RUN apt install libmariadb3 libmariadb-dev

WORKDIR /

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./api

ENV PYTHONUNBUFFERED 1

CMD [ "flask", "--app", "api", "run", "--host=0.0.0.0" ]