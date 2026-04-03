import csv_kezelo

fajl = "menu.csv"

class Menu:
    def __init__(self):
        self.etelek = csv_kezelo.beolvas(fajl)
    
    def listaz(self):
        print("\n____ ÉTLAP ____")
        for etel in self.etelek:
            print(f"{etel[0]} - {etel[1]} Ft")
    
    def hozzaad(self, nev, ar):
        self.etelek.append([nev, ar])
        csv_kezelo.kiment(fajl, self.etelek)
        print(f"{nev} hozzáadva az étlaphoz.")
    
    def torol(self, nev):
        eredeti = len(self.etelek)
        self.etelek = [e for e in self.etelek if e[0].lower() != nev.lower()]
        if len(self.etelek) < eredeti:
            csv_kezelo.kiment(fajl, self.etelek)
            print(f"{nev} törölve az étlapból.")
        else:
            print(f"{nev} nem található az étlapon.")
    
    def keres(self, nev):
        for etel in self.etelek:
            if etel[0].lower() == nev.lower():
                return etel
        return None