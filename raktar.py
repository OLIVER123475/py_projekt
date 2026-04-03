import csv_kezelo

fajl = "raktar.csv"

class Raktar:
    def __init__(self):
        self.keszlet = csv_kezelo.beolvas(fajl)
    
    def listaz(self):
        print("\n--- RAKTÁRKÉSZLET ---")
        for alapanyag in self.keszlet:
            print(f"{alapanyag[0]} - {alapanyag[1]} db")
    
    def csokkent(self, nev, mennyiseg):
        for alapanyag in self.keszlet:
            if alapanyag[0].lower() == nev.lower():
                uj_mennyiseg = int(alapanyag[1]) - int(mennyiseg)
                if uj_mennyiseg < 0:
                    print(f"[FIGYELEM] {nev} készlet el fog fogyni!")
                    return False
                alapanyag[1] = uj_mennyiseg
                csv_kezelo.kiment(fajl, self.keszlet)
                return True
        print(f"[HIBA] {nev} nem található a raktárban.")
        return False