FROM python:2.7
ADD . /code
WORKDIR /code/
RUN pip install -r requirements.txt

EXPOSE 5000 5001 5002 5003 3306
