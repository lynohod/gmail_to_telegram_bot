#modules
import telebot
import html2text
from datetime import datetime, timedelta
from imap_tools import MailBox
from configparser import ConfigParser

#read config.ini
cfg = ConfigParser()
cfg.read('config.ini')

token = cfg.get('Default', 'token')
server = cfg.get('Default', 'imap_server')
gmail_login = cfg.get('Default', 'gmail_login')
gmail_pass = cfg.get('Default', 'gmail_pass')

#activate bot
bot = telebot.TeleBot(token)



HELP = """
- What is my purpose?
- Drop last email in tg chat?
- OMG...

Enter command: /check
"""

@bot.message_handler(commands=['check'])
def check(message):

    #get mail from mailbox
    with MailBox(server).login(gmail_login, gmail_pass, 'INBOX') as mailbox:
        for msg in mailbox.fetch(limit=1, reverse=True):

            #define msg 'to'
            txt_to = ''.join(msg.to)
            txt_str = ("Last msg to: ")
            txt_to_format = txt_str + txt_to

            #define msg 'date'
            txt_date = msg.date.strftime('%d.%m.%Y   %H:%M')
            txt_date_format = datetime.strftime(datetime.strptime(txt_date, '%d.%m.%Y   %H:%M') + timedelta(hours=3), '%d.%m.%Y   %H:%M')

            #define body of msg
            txt_msg = html2text.html2text(msg.html)
            txt_msg_format = txt_msg[145:379]
    bot.send_message(message.chat.id, txt_to_format)
    bot.send_message(message.chat.id, txt_date_format)
    bot.send_message(message.chat.id, txt_msg_format)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(content_types=["text"])
def echo(message):
        bot.send_message(message.chat.id, "Enter command: /check")

# non stop requests to telegram servers
bot.polling(none_stop=True)
