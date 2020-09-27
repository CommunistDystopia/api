FROM python:3.8.6-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt ./requirements.txt

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers python3-dev musl-dev postgresql-dev
RUN pip install -r ./requirements.txt
RUN apk --no-cache add libpq
RUN apk update
RUN apk del .tmp

RUN mkdir /api
COPY . /api
WORKDIR /api
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web

RUN adduser -D user
RUN chown -R user:user /vol
RUN chown -R 755 /vol/web
USER user

CMD ["entrypoint.sh"]
