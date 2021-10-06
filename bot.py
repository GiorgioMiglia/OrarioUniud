
import logging

from telegram import Update, ForceReply, parsemode
from telegram.constants import PARSEMODE_MARKDOWN_V2
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from datetime import datetime

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


def send_command(update: Update, context: CallbackContext) -> None:  # this metod is used to send messages to the channel @informaticaUniud 
    update.message.reply_text('messaggio inviato')                   # used for important news
    context.bot.send_message(chat_id="@informaticauniud", text=update.message.text[5:])


def orario(update: Update, context: CallbackContext) -> None:  # this metod send the class schedule of the day (the day after if it's after the 19 GMT, or of monday if it's the weekend
    now=datetime.now()
    day=datetime.today().weekday()
    if(now.hour>18):
        day+=1
        string = "L'orario di domani è:\n"
    else :
        string = "L'orario di oggi è:\n"
    if(day > 4):
        string = "L'orario di Lunedì è:\n"
    string = string + str(orario1[day])
    update.message.reply_text(string, parse_mode=PARSEMODE_MARKDOWN_V2)
    

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("TOKEN")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("send", send_command))
    dispatcher.add_handler(CommandHandler("orario", orario))
    # on non command i.e message - echo the message on Telegram
    #dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

orario1 = [  "08:30\-10:30 *Analisi Matematica*    C1 \n10:30\-12:30 *Architettura degli Elaboratori*    C1  \n13:30\-15:30 *Programmazione*    C1 \n15:30\-17:30 *Architettura degli Elaboratori*    Laboratorio ",
            "10:30\-12:30 *Analisi Matematica*    C1  \n13:30\-15:30 *Architettura degli Elaboratori*    C1 \n15:30\-17:30 *Programmazione*    Laboratorio ",
            "Nessuna lezione",
            "10:30\-12:30 *Architettura degli Elaboratori*    Laboratorio  \n13:30\-15:30 *Programmazione*    C1 \n15:30\-17:30 *Matematica Discreta*    C1 ",          
            "10:30\-12:30 *Programmazione*    Laboratorio  \n13:30\-15:30 *Analisi Matematica*    C1 \n15:30\-17:30 *Matematica Discreta*    C2 ",     
        ]

if __name__ == '__main__':
    main()
