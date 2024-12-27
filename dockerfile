FROM python:3
ENV PYTHONBUFFERED=1
WORKDIR /django/onrec
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . . 
CMD gunicorn onRec.wsgi:application --bind 0.0.0.0:8000
EXPOSE 8000

