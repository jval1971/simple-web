FROM python:3.6.5-alpine3.7
ADD . /web
WORKDIR /web
RUN pip3 install -r requirements.txt
CMD ["python3", "web.py"]
