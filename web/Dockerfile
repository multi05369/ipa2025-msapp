FROM python

RUN pip install flask

COPY  ./static /home/myapp/static/

COPY  ./templates /home/myapp/templates/

COPY app.py /home/myapp/

COPY requirements.txt /home/myapp/

RUN pip install -r /home/myapp/requirements.txt

EXPOSE 8080

CMD python3 /home/myapp/app.py
