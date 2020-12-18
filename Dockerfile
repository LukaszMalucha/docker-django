FROM python:3.7-alpine

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev
RUN apk add jpeg-dev zlib-dev libjpeg
RUN pip install Pillow


RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

WORKDIR /usr/app
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]