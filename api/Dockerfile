FROM python:3.6.5-alpine3.7
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["python3", "api.py"]
