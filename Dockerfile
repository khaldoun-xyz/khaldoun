FROM python:3.11-alpine

WORKDIR '/app'

RUN apk add --no-cache \
    glib-dev \
    gobject-introspection-dev \
    cairo-dev \
    pango-dev \
    fontconfig \
    ttf-dejavu \
    && fc-cache -f -v

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY ./src .

EXPOSE 8000

CMD ["gunicorn", "khaldoun.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
