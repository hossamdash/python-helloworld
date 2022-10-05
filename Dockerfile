FROM python:3.8
LABEL maintaner="Hossam Mostafa"

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt
CMD [ "python", "app.py" ]