# base image
FROM python:3.10.7-slim-bullseye

WORKDIR /server

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./wait-for-it.sh .
COPY /server .

EXPOSE 5000

CMD ["python3", "sub.py"]
