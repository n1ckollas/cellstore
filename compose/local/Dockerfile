FROM python:2.7-buster

COPY ./r.txt r.txt
RUN pip install -r r.txt


RUN mkdir /cell_store
RUN mkdir /cell_store/staticfiles
RUN mkdir /cell_store/mediafiles

WORKDIR /cell_store

COPY . .

COPY ./compose/local/start.sh ./start.sh
RUN chmod +x ./start.sh



# ENTRYPOINT ["./start.sh"]
