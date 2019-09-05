FROM continuumio/miniconda3:4.6.14

WORKDIR /usr/src/app

ARG PORT=8000

COPY . .

RUN pip install -r requirements.txt

CMD ["sh", "entrypoint.sh"]

EXPOSE ${PORT}