FROM python:3.9-alpine
# RUN apt update && apt install -y gcc libmariadb-dev-compat
ENV PYTHONBUFFERED 1
RUN pip install gunicorn
WORKDIR /app
COPY Schedule /app
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .temp-build-deps \
        && apk add gcc libc-dev linux-headers postgresql-dev \
        && pip install --upgrade pip \
        && pip install -r requirements.txt \
        && apk del .temp-build-deps

EXPOSE 8000

CMD python manage.py makemigrations appsch
CMD python manage.py makemigrations
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "Schedule.wsgi"]