FROM continuumio/miniconda3:4.6.14

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn", "app:app", "--workers=5", "--threads=3"]