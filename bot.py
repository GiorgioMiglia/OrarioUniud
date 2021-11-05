#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

import logging
import queue
from telegram import Update, ForceReply, parsemode
from telegram.constants import PARSEMODE_MARKDOWN_V2
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from datetime import datetime, time
import pytz
import subprocess
import menu, dati, private

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Ciao {user.mention_markdown_v2()}\!',
    )


def send_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /send is issued."""
    update.message.reply_text('messaggio inviato')
    context.bot.send_message(chat_id="@informaticauniud", text=update.message.text[5:])
    #vedi issue numero 140 della libreria


def getOrario(update: Update, context: CallbackContext) -> None:  # * si potrebbe riscrivere per usare un metodo a sé per
    now=datetime.now(pytz.timezone('Europe/Rome'))             # * ottenere il giorno richiesto in modo da usarlo anche per getMenu 
    day=datetime.today().weekday()
    text=update.message.text[8:]
    if text.lower() in dati.settimana:
        string = "L'orario di " + text +" è:\n"
        day = dati.settimana.index(text.lower())
    else :
        if text.lower()=="domani" or (now.hour>17 and text == ""):
            day+=1
            string = "L'orario di domani è:\n"
        elif text.lower() == "ieri":
            day -=1
            string = "L'orario di ieri era:\n"
            if day<0:
                string = "Nessuna lezione nel weekend\. \nL'orario di Lunedì era:\n"
        else :
            string = "L'orario di oggi è:\n"
    if(day > 4):
        string = "Nessuna lezione nel weekend, la prossima lezione è Lunedì\. \nL'orario di Lunedì è:\n"
        day = 0
    string = string + str(dati.orario[day])
    update.message.reply_text(string, parse_mode=PARSEMODE_MARKDOWN_V2)
    

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(dati.helptxt, parse_mode=PARSEMODE_MARKDOWN_V2)


def link(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(private.linkList, parse_mode=PARSEMODE_MARKDOWN_V2)


def sendDailyTimetable(context: CallbackContext) :
    global oldId 
    if (oldId != 0):
        context.bot.delete_message(chat_id = "@informaticauniud" ,   message_id = oldId)
    day=datetime.today().weekday()
    string = "L'orario di oggi è:\n" + str(dati.orario[day])
    msg = context.bot.send_message(chat_id="@informaticauniud", text=string, parse_mode=PARSEMODE_MARKDOWN_V2)
    oldId = msg.message_id


def up(update: Update, context: CallbackContext) :
    if update.effective_chat.id==private.adminID :
        context.bot.send_message(chat_id=private.adminID, text="Aggiornamento in corso...")
        subprocess.call("./pull.sh", shell=True)
    else :
        string = update.effective_user + " ha mandato al bot il messaggio:\n" + update.message.text
        context.bot.send_message(chat_id=private.adminID, text=string)


def getMenu(update: Update, context: CallbackContext): # todo : aggiungere la possibilità di chiedere il menù di un giorno specifisco
    week = menu.getWeek()
    day = datetime.today().weekday()
    if (day>4):
        update.message.reply_text("La mensa è chiusa nel fine settimana", parse_mode=PARSEMODE_MARKDOWN_V2)
    else:
        update.message.reply_text("*PRIMI:*\n" + week["PRIMO"][day], parse_mode=PARSEMODE_MARKDOWN_V2)
        update.message.reply_text("*SECONDI:*\n" + week["SECONDO"][day], parse_mode=PARSEMODE_MARKDOWN_V2)
        update.message.reply_text("*CONTORNI:*\n" + week["CONTORNO"][day], parse_mode=PARSEMODE_MARKDOWN_V2)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(private.token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("send", send_command))
    dispatcher.add_handler(CommandHandler("orario", getOrario))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("link", link))
    dispatcher.add_handler(CommandHandler("update", up))
    dispatcher.add_handler(CommandHandler("menu", getMenu))


    # on non command i.e message - echo the message on Telegram
    #dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    #job queue to send timed messages
    jQueue = updater.job_queue

    jQueue.run_daily(sendDailyTimetable, time(hour=8, minute=0, tzinfo=pytz.timezone('Europe/Rome')) , days=(0,1,2,3,4))
    # Start the Bot
    updater.start_polling()
  
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

oldId = 0





if __name__ == '__main__':
    main()
