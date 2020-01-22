FROM python:alpine3.7
COPY ./api /api
WORKDIR /api
RUN pip install flask-restplus 
RUN pip install flask 
RUN pip install pymongo
EXPOSE 8887
CMD python run.py
