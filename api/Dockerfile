FROM python:3.10

WORKDIR /src
COPY . .

RUN pip install -r requirements.txt

CMD ["uwsgi" "--socket" "0.0.0.0:5000" "--protocol=http" "-w" "wsgi:app"]
