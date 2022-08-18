FROM ubuntu:latest
MAINTAINER Your Name 'your_email@email.com'
RUN apt-get update -qy
RUN apt-get install -qy python3-venv python3-pip
RUN pip3 install pyTelegramBotAPI
RUN pip3 install --upgrade pyTelegramBotAPI

COPY . /gmail_to_telegram_bot
WORKDIR /gmail_to_telegram_bot
RUN pip install -r requirements.txt
CMD ["python3","bot.py"]
