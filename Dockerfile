FROM ubuntu:latest

RUN apt clear && \
    apt update && \
    apt install python3 python3-pip -y &&
    rm -rf /var/lib/apt/lists/*
RUN pip3 install pyTelegramBotAPI

COPY . /gmail_to_telegram_bot
WORKDIR /gmail_to_telegram_bot
RUN pip install -r requirements.txt
CMD ["python3","bot.py"]
