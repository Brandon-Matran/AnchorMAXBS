FROM python:3.10-bullseye
RUN python -m pip install --upgrade pip
WORKDIR /app


COPY requirements.txt requirements.txt
COPY main.py main.py
COPY queries queries
COPY routers routers
COPY auth.py auth.py
COPY migrations migrations

RUN python -m pip install -r requirements.txt

CMD python -m migrations up && uvicorn main:app --host 0.0.0.0 --port 8000
