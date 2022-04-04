from bot import helpMenu


primiFissi = "Pasta o riso: \n\-al ragù di manzo \n\-al pomodoro \n\-in bianco"
secondiFissi = "Formaggi freschi confezionati"
contorniFissi = "Bis di contorni crudi"

settimana1Au = {
    "PRIMO" : ["Gnocchi friulani \n" + primiFissi, 
                "Pasta integrale alle melanzane e Taleggio \nPassato di verdure \n" + primiFissi, 
                "Tagliatelle mare e monti \n" + primiFissi, 
                "Lasagne alle verdure \nZuppa di legumi \n" + primiFissi,
                "Risotto con i piselli \n" + primiFissi],
    "SECONDO" : ["Scaloppine di suino alla pizzaiola \nPolpette di soia \nTacchino ai ferri \n" + secondiFissi,
                 "Frittata alle zucchine \nFettina di pollo al curry \nFiletto di trota ai ferri \n" + secondiFissi,
                 "Arrosto di tacchino \nFalafel \nBraciola di suino ai ferri \nTagliere di salumi \n" + secondiFissi,
                 "Filetto di platessa alla mugnaia \nTrota salata con verdure, mozzarella e uova \nBurger di bovino ai ferri \n" + secondiFissi,
                 "Spezzatino di vitello alla carnica \nUova al pomodoro \nFettina di pollo ai ferri \n" + secondiFissi],
    "CONTORNO" : ["Crocchette di patate \nMacedonia di verdure \n" + contorniFissi,
                  "Patate alla triestina \nBieta al vapore \n" + contorniFissi + "\nDolce",
                  "Patate gratinate \nFagiolini al vapore \n" + contorniFissi,
                  "Patate fritte \nFunghi trifolati \n" + contorniFissi + "\nDolce",
                  "Patate al rosmarino \nPiselli in tecia \n" + contorniFissi ]
}

settimana2Au = {
    "PRIMO" : ["Ravioli di magro panna e prosciutto cotto \n" + primiFissi,
               "Crema di zucchine e menta \nPasta al radicchio \n" + primiFissi,
               "Risotto alla parmigiana \n" + primiFissi,
               "Zuppa di risi e bisi \nPasta aglio, olio e peperoncino \n" + primiFissi,
               "Spatzle al burro ed erba cipollina \n" + primiFissi],
    "SECONDO" : ["Calamari alla Gardesana con crostini di pane \nPiadina alle verdure \nBurger di tacchino ai ferri\n" + secondiFissi,
                 "Coniglio al forno \nFrico di patate filante \nFiletto di sgombro ai ferri \n" + secondiFissi,
                 "Scaloppina di pollo alla senape \nBurger di orzo e verdure \nFettina di suino ai ferri \nTagliere di salumi \n" + secondiFissi,
                 "Salsiccia al forno \nOmelette di radicchio \nFettina di bovino ai ferri \n" + secondiFissi,
                 "Filetto di salmone al forno \nPomodori farciti \(olive, capperi, Grana Padano\) \nFettina di pollo ai ferri \n" + secondiFissi],
    "CONTORNO" : ["Crocchette di patate \nBroccoli al vapore \n" + contorniFissi +"\nDolce",
                  "Patate in tecia \nFinocchi gratinati \n" + contorniFissi,
                  "Purè di patate \nFagiolini al pomodoro \n" + contorniFissi + "\nDolce",
                  "Patate prezzemolate \nCarote all'olio \n" + contorniFissi,
                  "Patate alla paprika \nCavolini di Bruxelles al burro \n" + contorniFissi ]
}

settimana3Au = {
    "PRIMO" : ["Pasta al tonno olive e capperi \n" + primiFissi,
               "Crema di zucca \nRisotto alla salsiccia \n" + primiFissi,
               "Pasta ai formaggi \n" + primiFissi,
               "Orzo e fagioli \nCannelloni di carne al forno \n" + primiFissi,
               "Pasta alla panna e speck \n" + primiFissi],    
    "SECONDO" : ["Wurstel farciti \(formaggio e pancetta\) \nFiletto di merluzzo alla mediterranea \nFettina di bovino ai ferri \n" + secondiFissi,
                 "Frittata \nSeppie in umido alla veneta \nFettina di suino ai ferri \n" + secondiFissi,
                 "Spezzatino di bovino ai ferri \nFalafel \nFiletto di trota ai ferri \nTagliere di salumi \n" + secondiFissi,
                 "Fettina di suino alla milanese \nPiadina con verdure \nFettina di pollo ai ferri \n" + secondiFissi,
                 "Scaloppine di bovino alla pizzaiola \nUova strapazzate \nTrancio di salmone ai ferri \n" + secondiFissi],  
    "CONTORNO" : ["Purè di patate \nFagiolini all'olio \n" + contorniFissi,
                  "Patate alla triestina \nSpinaci al vapore \n" + contorniFissi + "\nDolce",
                  "Patate al vapore \nCarote al burro \n" + contorniFissi,
                  "Patatine fritte \nZucchine trifolate \n" + contorniFissi +"\nDolce",
                  "Patate al forno \nMacedonia di verdure \n" + contorniFissi]  
}

settimana4Au = {
    "PRIMO" : ["Risotto alla zucca \n" + primiFissi,
               "Crema di funghi con crostini \nTagliatelle all'amatriciana \n" + primiFissi,
               "Gnocchi al pomodoro e ricotta \n" + primiFissi,
               "Minestrone di verdure \nPasta al salmone e pomodorini \n" + primiFissi,
               "Pasta all'arrabbiata \n" + primiFissi],
    "SECONDO" : ["Grigliata mista \(salsiccia e suino\) \nFish & Chips \(con Merluzzo\) \nBurger di tacchino ai ferri \n" + secondiFissi,
                 "Filetto di sgombro al forno \nInvoltini di prosciutto e formaggio \nFettina di pollo ai ferri \n" + secondiFissi,
                 "Uova al pomodoro \nCosce di pollo al forno \nBurger di trota ai ferri \nTagliere di salumi \n" + secondiFissi,
                 "Scaloppina di tacchino ai funghi \nFrico \nFettina di suino ai ferri \n" + secondiFissi,
                 "Caciucco alla livornese \nPolpette di riso e piselli \nFettina di bovino ai ferri \n" + secondiFissi],
    "CONTORNO" : ["Patate alla paprika \nCarote prezzemolate \n" + contorniFissi + "\nDolce",
                  "Crocchette di patate \nBieta al limone\n" + contorniFissi,
                  "Purè di patate \nPiselli in umido \n" + contorniFissi + "\nDolce",
                  "Patate al pomodoro \nCavolfiori gratinati \n" + contorniFissi,
                  "Patate al rosmarino \nFagiolini al pomodoro \n" + contorniFissi],
}
# todo: menu primaverile, estivo

settimana1In = {
    "PRIMO" : ["Pasta salsciccia e zafferano \n" + primiFissi,
               "Pasta all'arrabbiata \n" + primiFissi,
               "Lasagne al ragù di manzo  \nMinestrone \n" + primiFissi,
               "Pasta ai frutti di mare \n" + primiFissi,
               "Orzotto ai funghi e speck \nMinestra di carote \n"+ primiFissi],
    "SECONDO" : ["Grigliata mista di carne \nPolpette di soia \nFiletto di trota ai ferri \n" + secondiFissi,
                 "Filetto di merluzzo dorato \nUova strapazzate \nPetto di pollo ai ferri \n" + secondiFissi,
                 "Cosce di pollo alla diavola \nPiadina alle verdure \nFettina di bovino ai ferri \nTagliare di salumi tipici \n" + secondiFissi,
                 "Seppie con piselli \nRotolo di frittata con formaggi \nBurger di tacchino ai ferri \n" + secondiFissi,
                 "Goulasch di bovino \nFocaccia farcita con pomodorini o verdure e mozzarella \nFiletto di sgombro ai ferri \n" + secondiFissi],
    "CONTORNO" : ["Crocchette di patate \nFagiolini al pomodoro \n" + contorniFissi,
                  "Patate al forno \nSpinaci al vapore \n" + contorniFissi + "\nDolce",
                  "Purè \nCavolfiori gratinati \n" + contorniFissi,
                  "Patate gratinate \nZucchine trifolate \n" + contorniFissi + "\nDolce",
                  "Patate in tecia \nCarote prezzemolate \n" + contorniFissi]
}
                 
settimana2In = {
    "PRIMO" : ["Pasta ricotta e pomodoro \n" + primiFissi,
                "Pasta integrale prosciutto cotto e panna \nCrema di piselli \n" + primiFissi,
                "Ricciole di ricotta e spinaci \n" + primiFissi,
                "Tagliatelle all'amatriciana \nCrema di zucchine e menta \n" + primiFissi,
                "Risotto al radicchio \n" + primiFissi],
    "SECONDO" : ["Braciola di suino tex mex \nFalafel \nTrancio di salmone ai ferri \n" + secondiFissi,
                 "Straccetti di pollo al curry \nStrudel di verdure \nFettina di suino ai ferri \n" + secondiFissi,
                 "Caciucco alla livornese con crostini \nUova al pomodoro \nFettina di tacchino ai ferri \nTagliere di salumi \n" + secondiFissi,
                 "Hamburger di bovino alla pizzaiola \nFrico di patate \nFiletto di sgombro ai ferri \n" + secondiFissi,
                 "Costa di suino \nCous cous con verdure \nFettina di manzo ai ferri \n" + secondiFissi],
    "CONTORNO" : ["Patate fritte \nBieta all'agro \n" + contorniFissi + "\nDolce",
                  "Patate prezzemolate \nFinocchi gratinati \n" + contorniFissi,
                  "Patate al forno \nMacedonia di verdure \n" + contorniFissi + "\nDolce",
                  "Patate alla paprika \nBroccoli al vapore \n" + contorniFissi,
                  "Purè \nFagioli in tecia \n" + contorniFissi],
}

settimana3In = {
    "PRIMO" : ["Spazle di spinaci alla panna \nZuppa di verdura \n" + primiFissi,
               "Pasta al salmone e pomodorini \n" + primiFissi,
               "Orzotto prosciutto e piselli \n" + primiFissi,
               "Pasta aglio olio e peperoncino \nMinestra di fagioli \n"  + primiFissi,
               "Pasta alla puttanesca \n" + primiFissi],
    "SECONDO" : ["Platessa alla mugnaia \nPiadina di verdure \nBurger di tacchino ai ferri \n" + secondiFissi,
                 "Fuselli di pollo al forno \nFrittata di formaggio \nPesce spada ai ferri \n" + secondiFissi,
                 "Spalla di suino arrosto \nTorta salata \nFettina di manzo ai ferri \nTagliere di salumi \n" + secondiFissi,
                 "Coniglio alle erbe aromatiche \nPolpette riso e piselli \nBurger di trota ai ferri \n" + secondiFissi,
                 "Totani fritti \nUova al pomodoro \nBraciola di suino ai ferri \n" + secondiFissi],
    "CONTORNO" : ["Patate al rosmarino \nCavoletti di Bruxell all'olio \n" + contorniFissi,
                  "Purè \nMais e carote al burro \n" + contorniFissi +"\nDolce",
                  "Crocchette di patate \nLenticchie al pomodoro \n" + contorniFissi,
                  "Patate alla triestina \nSpinaci al vapore \n"  + contorniFissi + "\nDolce",
                  "Patate prezzemolate \nCavolfiori gratinati \n" + contorniFissi]
}

settimana4In = {
    "PRIMO" : ["Tagliatelle al pomodore e funghi \n" + primiFissi,
                "Gnocchi alla romana \nZuppa di lenticchie \n" + primiFissi,
                "Risotto zucca e robiola \n" + primiFissi,
                "Pasta integrale alle verdure e zafferano \n" + primiFissi,
                "Pasta tonno e olive \nVellutata piccante \n" + primiFissi],
    "SECONDO" : ["Bocconcini di vitello in camicia \nUova strapazzate \nFiletto di sgombro ai ferri \n" + secondiFissi,
                 "Fettina di suino alla milanese \nPomodori ripieni \nFettina di tacchino ai ferri \n" + secondiFissi,
                 "Salsiccia al forno \nOmelette ricotta e spinaci \nFiletto di troata ai ferri \nTagliere di salumi \n" + secondiFissi,
                 "Scaloppina di pollo alla senape \nFalafel \nFettina di suino ai ferri \n" + secondiFissi,
                 "Filetto di salmone al limone \nFrico di patate \nFettina di bovino ai ferri \n" + secondiFissi],
    "CONTORNO" : ["Purè \nMacedonia di verdure \n" + contorniFissi + "\nDolce",
                  "Patate fritte \nPiselli in tecia \n" + contorniFissi,
                  "Patate alla paprika \nBroccoli gratinati \n" + contorniFissi + "\nDolce",
                  "Patate al rosmarino \nFinocchi al burro \n" + contorniFissi,
                  "Patate sabbiosa \nCarote prezzemolate \n" + contorniFissi]
}              


helpMenu = ("Con il ridotto puoi prendere:\n"
             "- Pizza, contorno\n"
             "- Pizza, dolce\n"
             "- Primo, pane, contorno, dolce\n"
             "- Secondo, pane, contorno dolce\n"
             "\n"
             "Con l'intero puoi prendere:\n"
             "- Pizza, contorno, dolce\n"
             "- Primo, secondo, pane, contorno, dolce\n\n"
             "Al posto del dolce si può prendere un buono per uno frozen jogurt al bar Yellow Pecora (chiedere in cassa)"
             )

settimaneAutunno = [settimana2Au, settimana3Au, settimana4Au, settimana1Au]
settimaneInverno = [settimana3In, settimana4In, settimana1In, settimana2In] #gli array sono stati riordinati


def getWeek(weekNumber):
    x = (weekNumber)%4
    if weekNumber in range(2, 13): #20 è un numero arbitrario sufficentemente grande
        return settimaneInverno[x]
    elif weekNumber in range(14, 30):
        return ""
    return settimaneAutunno[x]
