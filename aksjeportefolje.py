class Aksje():
    def __init__(self, navn:str, antall:int, kjopspris:float, naapris:float):
        self.navn = navn
        self.antall = antall
        self.kjopspris = kjopspris
        self.naapris = naapris

    def __str__(self) -> str:
        return f"{self.navn}: {self.antall} aksjer, {self.naapris}kr (kjøpt for {self.kjopspris}kr)"

    def verdinaa(self) -> float:
        return self.antall * self.naapris

    def verdida(self) -> float:
        return self.antall * self.kjopspris

class Portefolje():
    def __init__(self):
        self.aksjer = []
    
    def legg_til_aksje(self, filnavn, antall:int):
        priser = les_aksjekurs(filnavn)
        kjopspris = priser[0]
        naapris = priser[-1]
        navn = filnavn.replace(".txt","")
        aksje = Aksje(navn, antall, kjopspris, naapris)
        self.aksjer.append(aksje)
        print(f"La til {aksje} i porteføljen.")
    
    def kontoverdi(self):
        return sum(aksje.verdinaa() for aksje in self.aksjer)

    def vis_oversikt(self):
        for aksje in self.aksjer:
            print(aksje)
        print(f"Totalverdi i porteføljen: {self.kontoverdi()}kr")
    
def les_aksjekurs(filnavn):
    aksjekurs = []
    with open(filnavn, "r") as fil:
        for tall in fil:
            aksjekurs.append(round(float(tall.strip("[]\n")), 3))
    return aksjekurs



p = Portefolje()
p.legg_til_aksje("AAPL.txt", 100)
p.vis_oversikt()

