FROM python:3.12-slim
ENV PYTHONBUFFERED=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# system dependencies for Postgres
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . . 
RUN python3 manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "onRec.wsgi:application", "--bind", "0.0.0.0:8000"]