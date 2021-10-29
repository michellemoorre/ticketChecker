FROM python:3.8

WORKDIR /enter

COPY . .

RUN pip install Flask

CMD ["flask", "run"]