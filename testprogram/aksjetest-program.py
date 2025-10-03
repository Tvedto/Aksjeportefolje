import matplotlib.pyplot as plt

def les_inn_aksjekurser(filnavn):
    priser = []
    with open(filnavn, "r") as fil:
        for tall in fil:
            priser.append(float(tall.strip()))
    return priser

fil = "apple_sin_aksjekurs.txt"
priser = les_inn_aksjekurser(fil)

def hent_gjennomsnitt_siste_n_dager(liste, antall_dager:int):

    siste_n = liste[-antall_dager:]
    gjennomsnitt = sum(siste_n)/antall_dager

    return gjennomsnitt


def gjennomsnitt_graf_paa_n_dager(liste, antall_dager:int):
    gjennomsnitt = []
    for i in range(len(priser)):
        if i+1 < antall_dager:
            gjennomsnitt.append(None)
            continue
    
        siste_n = liste[i+1 -antall_dager : i+1]

        gjennomsnitt.append(sum(siste_n) / antall_dager)
    
    return gjennomsnitt


def kjop_selg(priser, gjennomsnittspriser, antall_dager):
    innvestert = 0
    aksje = 0
    kjop = 0
    tjent = 0
    aksjersolgt = 0
    stop_prosent = 0.05
    profit_prosent = 0.2

    for i in range(antall_dager, len(priser)):
        if gjennomsnittspriser[i] is None:
            continue

        aksjevekt = 1 + ((gjennomsnittspriser[i] - priser[i]) / gjennomsnittspriser[i])*100
        aksjevekt = int(max(1, round(aksjevekt)))



        if all(p < gjennomsnittspriser[i] for p in priser[i-1:i+1]):
            kjop += priser[i]*aksjevekt
            aksje += aksjevekt
            #print(f"Kjoper {aksjevekt:.2f} aksjer til prisen {priser[i]:.2f}kr")

        elif aksje > 0:
            aksjeverdi = priser[i] * aksje
            if aksjeverdi <= kjop * (1- stop_prosent): 
                selg = aksje * priser[i]
                #print(f"Selger {aksje:.2f} aksje(r) til prisen {priser[i]:.2f}kr")
                gevinst = selg - kjop
                aksjersolgt += aksje
                tjent += gevinst
                #print(f"Tjent paa denne handelen: {gevinst:.2f}")
                
                innvestert += kjop
                aksje = 0
                kjop = 0
            elif aksjeverdi >= kjop * (1 - profit_prosent):
                selg = aksje * priser[i]
                #print(f"Selger {aksje:.2f} aksje(r) til prisen {priser[i]:.2f}kr")
                gevinst = selg - kjop
                aksjersolgt += aksje
                tjent += gevinst
                #print(f"Tjent paa denne handelen: {gevinst:.2f}")
                
                innvestert += kjop
                aksje = 0
                kjop = 0                

    if aksje > 0:
        sluttverdi = aksje * priser[-1]
        gevinst = sluttverdi - kjop
        tjent += gevinst
        aksjersolgt += aksje
        innvestert += kjop
        print(f"Avslutter: selger {aksje:.2f} aksje(r) til prisen {priser[-1]}kr.\nTjent paa denne handelen {gevinst}")

    print(f"Totalt innvestert: {innvestert:.2f}kr. Totalt aksjer solgt {aksjersolgt}. Gevinst per aksje: {tjent/aksjersolgt if aksjersolgt else 0:.2f}kr.\nTotalt tjent: {tjent:.2f}kr. Prosent økning: {(((innvestert+tjent)/aksjersolgt if aksjersolgt else 0)/priser[0])*100:.2f}%")


def vektet_gjennomsnitt(priser, kort=3, langt=10, vekt=0.8):
    kort_snitt = gjennomsnitt_graf_paa_n_dager(priser, kort)
    langt_snitt = gjennomsnitt_graf_paa_n_dager(priser, langt)
    gjennomsnitt = []
    for i in range(len(priser)):
        if kort_snitt[i] is None or langt_snitt[i] is None:
            gjennomsnitt.append(None)
            continue
        verdi = vekt * kort_snitt[i] + (1-vekt) * langt_snitt[i] 
        gjennomsnitt.append(verdi)

    return gjennomsnitt

def buy_and_hold(priser):
    okning = (priser[-1] / priser[0]) * 100
    return f"{okning:.2f}%"

def kryss_strategi(priser, kort=20, langt=100):
    kort_snitt = gjennomsnitt_graf_paa_n_dager(priser, kort)
    langt_snitt = gjennomsnitt_graf_paa_n_dager(priser, langt)

    aksje = 0
    penger = 10000  # starter med 10 000 kr
    for i in range(len(priser)):
        if kort_snitt[i] is None or langt_snitt[i] is None:
            continue

        if kort_snitt[i] > langt_snitt[i] and aksje == 0:
            aksje = penger / priser[i]
            penger = 0

        elif kort_snitt[i] < langt_snitt[i] and aksje > 0:
            penger = aksje * priser[i]
            aksje = 0

    if aksje > 0:
        penger = aksje * priser[-1]

    avkastning = (penger / 10000 - 1) * 100
    return f"{avkastning:.2f}%"






antall_dager = 10
gjennomsnitt = vektet_gjennomsnitt(priser)
algogevinst = kryss_strategi(priser)
holdgevinst = buy_and_hold(priser)


print(f"Buy and hold: {holdgevinst}")
print(f"Algoritmebasert gevinst: {algogevinst}")

plt.plot(priser, label = "Pris")
plt.plot(gjennomsnitt, label = str(antall_dager)+"-dagers snitt")
plt.legend()
plt.show()