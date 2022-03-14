FROM python:3.8.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000
ENV SECRET_KEY=os.environ.get("SECRET_KEY")

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

EXPOSE $PORT

CMD python ./manage.py runserver 0.0.0.0:$PORT