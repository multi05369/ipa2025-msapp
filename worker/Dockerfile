FROM python

WORKDIR /home/worker

COPY ./requirements.txt /home/worker/

COPY ./database.py /home/worker/

COPY ./worker.py /home/worker/

COPY ./connection.py /home/worker/

RUN pip install -r ./requirements.txt

CMD ["python3", "worker.py"]
