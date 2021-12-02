from bot import helpMenu


primiFissi = "Pasta o riso: \n\-al ragù di manzo \n\-al pomodoro \n\-in bianco"
secondiFissi = "Formaggi freschi confezionati"
contorniFissi = "Bis di contorni crudi"

settimana1 = {
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

settimana2 = {
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
                  "Patate in tecia \n Finocchi gratinati \n" + contorniFissi,
                  "Purè di patate \nFagiolini al pomodoro \n" + contorniFissi + "\nDolce",
                  "Patate prezzemolate \nCarote all'olio \n" + contorniFissi,
                  "Patate alla paprika \nCavolini di Bruxelles al burro \n" + contorniFissi ]
}

settimana3 = {
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

settimana4 = {
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
# todo: menu invernale, primaverile, estivo


helpMenu = ("Con il ridotto puoi prendere:\n"
             "- Pizza (forse anche il dolce)\n"
             "- Primo, pane, contorno, dolce\n"
             "- Secondo, pane, contorno dolce\n"
             "\n"
             "Con l'intero puoi prendere:\n"
             "- Pizza, contorno, dolce\n"
             "- Primo, secondo, pane, contorno, dolce"
             )

settimana = [settimana1, settimana2, settimana3, settimana4]

def getWeek(weekNumber):
    x = (weekNumber+1)%4
    return settimana[x]
