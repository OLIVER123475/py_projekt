import csv_kezelo

fajl = "vasarlasok.csv"

class Vasarlok:
    def __init__(self):
        self.vasarlasok = csv_kezelo.beolvas(fajl)
    
    def listaz(self):
        print("\n--- LEZÁRT RENDELÉSEK ---")
        for v in self.vasarlasok:
            print(f"Vásárló: {v[0]} | Felszolgáló: {v[1]} | Végösszeg: {v[2]} Ft | Ételek: {', '.join(v[3:])}")
    
    def ment(self, vasarlo_nev, felszolgalo_nev, osszeg, etelek):
        uj_sor = [vasarlo_nev, felszolgalo_nev, osszeg] + etelek
        self.vasarlasok.append(uj_sor)
        csv_kezelo.kiment(fajl, self.vasarlasok)
        print(f"Rendelés elmentve! Végösszeg: {osszeg} Ft")