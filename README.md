# OrarioUniud
# Bot telegram scritto in python che fornisce l'orario del giorno per il primo anno del corso di studi di Informatica presso l'università di Udine
---------------------

Comandi disponibili :
- **/start** avvia il bot
- **/orario (msg)** fornisce l'orario del giorno, dopo le 17 dà quello del giorno dopo, accetta come **msg** _ieri, oggi, domani e i giorni della settimana_
- **/help** fornisce un messaggio con i comandi del bot
- **/link** fornisce link utili, come quelli del gruppo e dei canali associati
- **/send (msg)** manda **msg** nel canale associato, dà la possibilità agli utenti di mandare comunicazioni a tutti i membri del canale
- **/menu** fornisce il menù del giorno della mensa **(ancora in fase di test)**

Inoltre è disponibile il comando **/update** ad uso esclusivo dell'admin per aggiornare automaticamente il bot con il codice presente su github (vedere [pull.sh](https://github.com/GiorgioMiglia/OrarioUniud/blob/main/pull.sh)

Come è strutturato il bot:
- [bot.py](https://github.com/GiorgioMiglia/OrarioUniud/blob/main/bot.py) è il codice principale del bot con tutti i metodi necessari al suo funzionamento
- [dati.py](https://github.com/GiorgioMiglia/OrarioUniud/blob/main/dati.py) contiene dati utili, come l'orario o messaggi già pronti (per i comandi help e link)
- [menu.py](https://github.com/GiorgioMiglia/OrarioUniud/blob/main/menu.py) contiene i dati relativi al menù della mensa e i metodi necessari a selezionare la settimana giusta
- [pull.sh](https://github.com/GiorgioMiglia/OrarioUniud/blob/main/pull.sh) script per aggiornare il bot
- [private.py](https://www.youtube.com/watch?v=dQw4w9WgXcQ) contiene tutti i dati che è meglio non rendere pubblici, come il token o i chatId del gruppo e dell'admin, non è presente su Github (ma non dimenticarlo se vuoi fare un bot a partire da questo)
