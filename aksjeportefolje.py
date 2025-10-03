class Aksje():
    def __init__(self, navn, antall, kjopspris, naapris):
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
    
    def legg_til_aksje(self, navn:str, antall:int, kjopspris:float, naapris:float):
        aksje = Aksje(navn, antall, kjopspris, naapris)
        self.aksjer.append(aksje)
        print(f"La til {aksje} i porteføljen.")
    
    def kontoverdi(self):
        return sum(aksje.verdinaa() for aksje in self.askjer)

    def vis_oversikt(self):
        for aksje in self.aksjer:
            print(aksje)
        print(f"Totalverdi i porteføljen: {self.kontoverdi()}kr")
    

p = Portefolje()
p.legg_til_aksje("Apple", 10, 150, 175)
p.legg_til_aksje("Tesla", 5, 200, 180)
p.vis_oversikt()

