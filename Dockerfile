FROM marcelotokarnia/trackpedia:0.0.1

MAINTAINER Marcelo Tokarnia <marcelo.tokarnia@gmail.com>

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY docker/uwsgi.ini uwsgi.ini
COPY docker/uwsgi_params /uwsgi/uwsgi_params

ENTRYPOINT ["docker/entrypoint.sh"]
