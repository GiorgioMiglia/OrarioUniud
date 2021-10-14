#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

import logging
import queue
import private
from telegram import Update, ForceReply, parsemode
from telegram.constants import PARSEMODE_MARKDOWN_V2
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from datetime import datetime, time
import pytz

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
        fr'Hi {user.mention_markdown_v2()}\!',
    )


def send_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /send is issued."""
    update.message.reply_text('messaggio inviato')
    context.bot.send_message(chat_id="@informaticauniud", text=update.message.text[5:])
    #vedi issue numero 140 della libreria

def orario(update: Update, context: CallbackContext) -> None:
    now=datetime.now(pytz.timezone('Europe/Rome'))
    day=datetime.today().weekday()
    text=update.message.text[8:]
    if text.lower() in settimana:
        string = "L'orario di " + text +" è:\n"
        day = settimana.index(text.lower())
    else :
        if text.lower()=="domani" or (now.hour>17 and text == ""):
            day+=1
            string = "L'orario di domani è:\n"
        elif text.lower() == "ieri":
            day -=1
            if day>=0:
                string = "L'orario di ieri era:\n"
            else:
                string = "Nessuna lezione nel weekend, l'orario di Venderdì era:\n"
                day=4
        else :
            string = "L'orario di oggi è:\n"
    if(day > 4):
        string = "Nessuna lezione nel weekend, la prossima lezione è Lunedì\. \nL'orario di Lunedì è:\n"
        day = 0
    string = string + str(orario1[day])
    update.message.reply_text(string, parse_mode=PARSEMODE_MARKDOWN_V2)
    
def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(helptxt, parse_mode=PARSEMODE_MARKDOWN_V2)

def link(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(private.linkList, parse_mode=PARSEMODE_MARKDOWN_V2)

def sendDailyTimetable(context: CallbackContext) :
    day=datetime.today().weekday()
    string = "L'orario di oggi è:\n" + str(orario1[day])
    context.bot.send_message(chat_id="@informaticauniud", text=string, parse_mode=PARSEMODE_MARKDOWN_V2)

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(private.token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("send", send_command))
    dispatcher.add_handler(CommandHandler("orario", orario))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("link", link))

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

settimana = ["lunedì","martedì","mercoledì","giovedì","venerdì","sabato","domenica"]

orario1 = [  "08:30\-10:30 *Analisi Matematica*    C1 \n10:30\-12:30 *Arc\. degli Elaboratori*    C1  \n13:30\-15:30 *Programmazione*    C1 \n15:30\-17:30 *Arc\. degli Elaboratori*    Lab ",
            "10:30\-12:30 *Analisi Matematica*    C1  \n13:30\-15:30 *Arc\. degli Elaboratori*    C1 \n15:30\-17:30 *Programmazione*    Lab ",
            "Nessuna lezione",
            "10:30\-12:30 *Arc\. degli Elaboratori*    Lab  \n13:30\-15:30 *Programmazione*    C1 \n15:30\-17:30 *Matematica Discreta*    C1 ",          
            "10:30\-12:30 *Programmazione*    Lab  \n13:30\-15:30 *Analisi Matematica*    C1 \n15:30\-17:30 *Matematica Discreta*    C2 ",     
            "",
            ""
        ]

helptxt =( "Questo bot è dedicato al primo anno del corso di laurea in Informatica presso l'Università degli studi di Udine, " 
           "i comandi disponibili sono:\n"
           "*/help* \-\-  mostra questo messaggio\n"
           "*/orario \<giorno\>* \-\- mostra l'orario del giorno indicato, accetta in input anche *ieri*, *oggi*, *domani*\." 
           " Se omesso mostra l'orario del giorno o, dopo le 17, di quello successivo\n"
           "*/link* \-\- ottieni i link utili dei vari gruppi e delle risorse utili\n"
           "*/send \<msg\>* \-\- usato per note o comunicazioni importanti, manda \<msg\> nel canale @informaticaUniud"
)




if __name__ == '__main__':
    main()
