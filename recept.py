import csv_kezelo

fajl = "recept.csv"

class Recept:
    def __init__(self):
        self.receptek = csv_kezelo.beolvas(fajl)
    
    def get_alapanyagok(self, etel_nev):
        alapanyagok = []
        for sor in self.receptek:
            if sor[0].lower() == etel_nev.lower():
                alapanyagok.append({
                    "nev": sor[1],
                    "mennyiseg": int(sor[2])
                })
        return alapanyagok
    
    def hozzaad(self, etel_nev, alapanyag_nev, mennyiseg):
        self.receptek.append([etel_nev, alapanyag_nev, mennyiseg])
        csv_kezelo.kiment(fajl, self.receptek)
    
    def torol(self, etel_nev):
        self.receptek = [r for r in self.receptek if r[0].lower() != etel_nev.lower()]
        csv_kezelo.kiment(fajl, self.receptek)