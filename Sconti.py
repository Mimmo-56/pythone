def main():
    prezzi = []
    animale = []
    riga = input("Passami il prezzo e Y/N se animale : ")
    while riga != "":
        dati = riga.split(" ")
        prezzi.append(float(dati[0]))
        animale.append = dati[1]     
        riga = input("Passami il prezzo e Y/N se animale : ")
    sconti = sconto(prezzi, animale)

def sconto(prezzi, animale):
    sconto = 0
    for i in range(len(prezzi)):
        if animale[i] == "N":
            sconto += prezzi[i] * 0.2
    print("Il totale degli sconti è: ", sconto)
    return sconto
main()