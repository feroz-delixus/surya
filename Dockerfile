FROM python:3.10.1

WORKDIR /app

ADD ./.profile.d /app/.profile.d

COPY . .

RUN apt update && \
    apt install npm -y

RUN npm install -g surya

RUN surya --version

RUN pip install -r requirements.txt

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

#EXPOSE 5000

ENTRYPOINT ["python", "suryarestcall.py"]

#CMD bash heroku-exec.sh && python suryarestcall.py

