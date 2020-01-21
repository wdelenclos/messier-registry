FROM python:alpine3.7
COPY ./api /api
WORKDIR /api
RUN pip install flask-restplus flask pymongo
EXPOSE 8887
CMD python run.py