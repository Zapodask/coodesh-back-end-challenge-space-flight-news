FROM python:3.10

WORKDIR /api
COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:5000", "index:app", "-w", "4"]
