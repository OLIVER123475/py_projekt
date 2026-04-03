import csv_kezelo

class Rendeles:
    def __init__(self, asztal_szam, vasarlo_nev, felszolgalo_nev):
        self.asztal_szam = asztal_szam
        self.vasarlo_nev = vasarlo_nev
        self.felszolgalo_nev = felszolgalo_nev
        self.etelek = []      # rendelt ételek nevei
        self.osszeg = 0       # folyamatos összeg
    
    def hozzaad(self, etel, raktar, recept):
        # Megnézzük milyen alapanyag kell
        alapanyagok = recept.get_alapanyagok(etel[0])
        
        # Leellenőrizzük és levonjuk a raktárból
        for a in alapanyagok:
            if not raktar.csokkent(a["nev"], a["mennyiseg"]):
                print(f"[HIBA] Nem rendelhető: {etel[0]} - nincs elég alapanyag!")
                return False
        
        # Ha minden oke, hozzáadjuk a rendeléshez
        self.etelek.append(etel[0])
        self.osszeg += int(etel[1])
        print(f"{etel[0]} hozzáadva a rendeléshez. Jelenlegi összeg: {self.osszeg} Ft")
        return True
    
    def listaz(self):
        print(f"\n--- {self.asztal_szam}. ASZTAL RENDELÉSE ---")
        print(f"Vásárló: {self.vasarlo_nev} | Felszolgáló: {self.felszolgalo_nev}")
        for etel in self.etelek:
            print(f"  - {etel}")
        print(f"Jelenlegi összeg: {self.osszeg} Ft")
    
    def lezar(self, vasarlok):
        if not self.etelek:
            print("[HIBA] Nem lehet lezárni üres rendelést!")
            return False
        vasarlok.ment(self.vasarlo_nev, self.felszolgalo_nev, self.osszeg, self.etelek)
        print(f"Rendelés lezárva! Végösszeg: {self.osszeg} Ft")
        return True