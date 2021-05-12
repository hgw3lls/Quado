# backend/Dockerfile

FROM python:3.8-slim

WORKDIR /app

RUN apt-get update
#RUN apt-get install \
#    'xxx'\
#    'xxx'\
#    'xxx'  -y

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

# CMD ["uvicorn", "main:app", "host", "0.0.0.0" "--port", "$PORT"]
# CMD uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port $PORT

#CMD gunicorn -w 3 -k uvicorn.workers.UvicornWorker main:app

#CMD ["gunicorn", "-b", "0.0.0.0:\$PORT", "-w", "3", "-k", "uvicorn.workers.UvicornWorker", "main:app"]

 CMD gunicorn -b 0.0.0.0:8080 -w 3 -k uvicorn.workers.UvicornWorker main:app
# gunicorn -b 0.0.0.0:8080 -w 3 -k uvicorn.workers.UvicornWorker backend.main:app

# CMD uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8080


#web: uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000}

#gunicorn -b 0.0.0.0:8080 -w 3 -k uvicorn.workers.UvicornWorker backend.main:app
