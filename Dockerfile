FROM python:3.9.8

WORKDIR /app

COPY requirements.txt

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . .

ENTRYPOINT ["python", "app.py"]
