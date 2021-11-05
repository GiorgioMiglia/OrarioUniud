import private

orario = [  "08:30\-10:30 *Analisi Matematica*    C1 \n10:30\-12:30 *Arc\. degli Elaboratori*    C1  \n13:30\-15:30 *Programmazione*    C1 \n15:30\-17:30 *Arc\. degli Elaboratori*    Lab ",
            "10:30\-12:30 *Analisi Matematica*    C1  \n13:30\-15:30 *Arc\. degli Elaboratori*    C1 \n15:30\-17:30 *Programmazione*    Lab ",
            "Nessuna lezione",
            "10:30\-12:30 *Arc\. degli Elaboratori*    Lab  \n13:30\-15:30 *Programmazione*    C1 \n15:30\-17:30 *Matematica Discreta*    C1 ",          
            "13:30\-15:30 *Analisi Matematica*    C1 \n15:30\-17:30 *Matematica Discreta*    C2 " ]

settimana = ["lunedì","martedì","mercoledì","giovedì","venerdì","sabato","domenica"]

helptxt =( "Questo bot è dedicato al primo anno del corso di laurea in Informatica presso l'Università degli studi di Udine, " 
           "i comandi disponibili sono:\n"
           "*/help* \-\-  mostra questo messaggio\n"
           "*/orario \<giorno\>* \-\- mostra l'orario del giorno indicato, accetta in input anche *ieri*, *oggi*, *domani*\." 
           " Se omesso mostra l'orario del giorno o, dopo le 17, di quello successivo\n"
           "*/link* \-\- ottieni i link utili dei vari gruppi e delle risorse utili\n"
           "*/send \<msg\>* \-\- usato per note o comunicazioni importanti, manda \<msg\> nel canale @informaticaUniud\n"
           "*/menu* \-\- mostra il menu del giorno \(_BETA, se si dovessero riscontrare errori o incongruenze con il menù effettivo contattare [Giorgio](tg://user?id=" + str(private.adminID) + ")_\)"
)