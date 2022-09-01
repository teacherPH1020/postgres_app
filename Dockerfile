FROM python:latest

RUN apt-get update \
	&&  apt-get install mc -y \
	&& apt install git
	
WORKDIR /home

RUN git clone https://github.com/teacherPH1020/postgres_app.git 

WORKDIR /home/postgres_app

RUN pip install -r requirements.txt

EXPOSE 8000
	
ENV DATABASE_IP 172.18.0.2

COPY version.txt .

RUN mkdir /mnt/volume
VOLUME /mnt/volume

CMD ["python","/home/postgres_app/manage.py","runserver","0.0.0.0:8000"]
