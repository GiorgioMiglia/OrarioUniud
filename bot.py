#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

import logging
import queue
from telegram import Update, ForceReply, parsemode
from telegram.constants import PARSEMODE_MARKDOWN_V2
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from datetime import datetime, time, date
import pytz
import subprocess
import menu, dati, private

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

#* Metodi "generici"

def addToTxt(id):
    database=open('chatId.txt', 'r')
    lista=database.readlines()
    database.close()
    found=False
    for riga in lista:
        if str(id) in riga:
            found=True
            break
    if not found:
        database=open('chatId.txt', 'a')
        database.write(str(id)+'\n')
        database.close()

def getDay(text):
    day=datetime.today().weekday()
    now=datetime.now(pytz.timezone('Europe/Rome')) 
    week = 0
    text = text.lower()
    if text == '':
        if now.hour > 17:
            day += 1
    elif text in dati.settimana:
        day = dati.settimana.index(text)
    elif "domani" in text:
        day += 1
    elif "ieri" in text:
        day -= 1
    if day > 4:
        week = 1
        day = 0
    elif day < 0 :
        week = -1
        day = 4
    str = dati.settimana[day][:1].upper() + dati.settimana[day][1:]
    return day, week, str

oldId = 0

#* Metodi che compiono azioni in corrispondenza dei vari comandi inviati al bot, vedere dispatcher (righe 134-141)

def start(update: Update, context: CallbackContext) -> None:         # risponde al comando /start, raccoglie il chat id e dà il benvenuto all'utente sul bot
    user = update.effective_user
    addToTxt(str(update.effective_chat.id))
    update.message.reply_markdown_v2("Ciao "+ user.mention_markdown_v2()+"\! \nUsa /help per avere la lista dei possibili comandi")


def send_command(update: Update, context: CallbackContext) -> None:  #risponde a /send, manda il testo inviato dall'utente nel canale @informaticauniud
    update.message.reply_text('Invio messaggio in corso...')
    context.bot.send_message(chat_id="@informaticauniud", text=update.message.text[5:])
    #vedi issue numero 140 della libreria python-telegram-bot


def getOrario(update: Update, context: CallbackContext) -> None:  #risponde a /orario <msg>, fornisce l'orario del giorno indicato dall'utente o per il giorno corrente           
    update.message.reply_text("Questo orario si riferisce al primo semestre", parse_mode=PARSEMODE_MARKDOWN_V2)
    text=update.message.text[8:]
    day = getDay(text)
    string = "L'orario di " + day[2] +" è:\n"
    if day[1]:
        string = "Nessuna lezione nel weekend\. \nL'orario di " + day[2]+ " è:\n"
    string = string + str(dati.orario[day[0]])
    update.message.reply_text(string, parse_mode=PARSEMODE_MARKDOWN_V2)
    

def help(update: Update, context: CallbackContext) -> None:      #risponde a /help, fornisce il messaggio di aiuto (vedi help.txt su dati.py)
    update.message.reply_text(dati.helptxt, parse_mode=PARSEMODE_MARKDOWN_V2)


def link(update: Update, context: CallbackContext) -> None:      #risponde a /link, fornisce lista di link utili
    update.message.reply_text(private.linkList, parse_mode=PARSEMODE_MARKDOWN_V2)


def sendDailyTimetable(context: CallbackContext) :  # metodo invocato dal lunedì al venerdì alle 8:00 per inviare in automatico l'orario del giorno
    global oldId       #oldId mi serve per cancellare l'orario del giorno prima dal canale
    if (oldId != 0):
        context.bot.delete_message(chat_id = "@informaticauniud" ,   message_id = oldId)
    day=datetime.today().weekday()
    string = "L'orario di oggi è:\n" + str(dati.orario[day])
    msg = context.bot.send_message(chat_id="@informaticauniud", text=string, parse_mode=PARSEMODE_MARKDOWN_V2)
    oldId = msg.message_id

def helpMenu(update: Update, context: CallbackContext):
    update.message.reply_text( menu.helpMensa, parse_mode=PARSEMODE_MARKDOWN_V2)


def getMenu(update: Update, context: CallbackContext): # risponde a /menu <msg>, fornisce il menu del giorno indicato (vedi menu.py)
    day = getDay(update.message.text[6:])
    weekNumber = date.today().isocalendar()[1] + day[1]
    week = menu.getWeek(weekNumber)
    if week == "":
        update.message.reply_text("L'orario invernale non è ancora disponibile, se hai una foto del menù puoi inviarla a [Giorgio](tg://user?id=" + str(private.adminID) + ")", parse_mode=PARSEMODE_MARKDOWN_V2)
    else:
        if day[1] == -1:
            update.message.reply_text("La mensa è chiusa nel fine settimana\nIl menù di Venerdì era:", parse_mode=PARSEMODE_MARKDOWN_V2)
            day = 0
        elif day[1]:
            update.message.reply_text("La mensa è chiusa nel fine settimana\nIl menù di Lunedì sarà:", parse_mode=PARSEMODE_MARKDOWN_V2)
        update.message.reply_text("*PRIMI:*\n" + week["PRIMO"][day[0]], parse_mode=PARSEMODE_MARKDOWN_V2)
        update.message.reply_text("*SECONDI:*\n" + week["SECONDO"][day[0]], parse_mode=PARSEMODE_MARKDOWN_V2)
        update.message.reply_text("*CONTORNI:*\n" + week["CONTORNO"][day[0]], parse_mode=PARSEMODE_MARKDOWN_V2)


def up(update: Update, context: CallbackContext) :     #metodo disponibile solo per l'admin, risponde a /update e aggiorna il bot da github (vedi pull.sh)
    if update.effective_chat.id==private.adminID :
        context.bot.send_message(chat_id=private.adminID, text="Aggiornamento in corso...")
        subprocess.call("./pull.sh", shell=True)
    else :
        string = update.effective_user + " ha mandato al bot il messaggio:\n" + update.message.text
        context.bot.send_message(chat_id=private.adminID, text=string)


def getTotalUsers(update: Update, context: CallbackContext): #riservato all'admin, fornisce una stima degli utenti attivi
    if update.effective_chat.id==private.adminID :
        database=open('chatId.txt', 'r')
        lista=database.readlines()
        database.close()
        context.bot.send_message(chat_id=private.adminID, text="Ci sono " + str(len(lista)) + " utenti")      

#* Metodo main che gestisce l'avvio dei metodi per i vari comandi 

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
    dispatcher.add_handler(CommandHandler("user", getTotalUsers))
    dispatcher.add_handler(CommandHandler("helpmensa", helpMenu))


    # on non command i.e message - echo the message on Telegram
    #dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    #job queue to send timed messages
    jQueue = updater.job_queue

    #* Disabilitato fino a inizio lezioni secondo semestre (01/03/2022)
    #* jQueue.run_daily(sendDailyTimetable, time(hour=8, minute=0, tzinfo=pytz.timezone('Europe/Rome')) , days=(0,1,2,3,4))
    # Start the Bot
    updater.start_polling()
  
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()






if __name__ == '__main__':
    main()
