FROM marcelotokarnia/trackpedia:0.0.1

WORKDIR /app

ADD . /app

RUN apt-get install -y git

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN . .env

EXPOSE 8000

ENV NAME Trackpedia

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
