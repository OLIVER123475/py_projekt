#tobbi fajl importalasa
import menu
import vasarlok
import raktar
import recept
from rendeles import Rendeles

def main():
    etlap = menu.Menu()
    raktarkeszlet = raktar.Raktar()
    receptek = recept.Recept()
    vasarlasok = vasarlok.Vasarlok()
    
    # Az aktív rendelések asztalonként tárolása
    aktiv_rendelesek = {}

    while True:
        #Rendelési opciók
        print("\n=== ÉTTERMI RENDELŐ ===")
        print("1. Új rendelés nyitása")
        print("2. Étel hozzáadása rendeléshez")
        print("3. Rendelés megtekintése")
        print("4. Rendelés lezárása")
        print("5. Étlap kezelése")
        print("6. Raktár megtekintése")
        print("7. Lezárt rendelések listája")
        print("0. Kilépés")

        valasztas = input("\nVálassz: ").strip()

        if valasztas == "1":
            asztal = int(input("Asztal száma: "))
            if asztal in aktiv_rendelesek:
                print("[HIBA] Ennek az asztalnak már van aktív rendelése!")
            else:
                vasarlo = input("Vásárló neve: ")
                felszolgalo = input("Felszolgáló neve: ")
                aktiv_rendelesek[asztal] = Rendeles(asztal, vasarlo, felszolgalo)
                print(f"{asztal}. asztal rendelése megnyitva!")

        elif valasztas == "2":
            asztal = int(input("Asztal száma: "))
            if asztal not in aktiv_rendelesek:
                print("[HIBA] Nincs aktív rendelés ennél az asztalnál!")
            else:
                etlap.listaz()
                etel_nev = input("Étel neve: ").strip()
                etel = etlap.keres(etel_nev)
                if etel is None:
                    print("[HIBA] Ez az étel nem szerepel az étlapon!")
                else:
                    aktiv_rendelesek[asztal].hozzaad(etel, raktarkeszlet, receptek)

        elif valasztas == "3":
            asztal = int(input("Asztal száma: "))
            if asztal not in aktiv_rendelesek:
                print("[HIBA] Nincs aktív rendelés ennél az asztalnál!")
            else:
                aktiv_rendelesek[asztal].listaz()

        elif valasztas == "4":
            asztal = int(input("Asztal száma: "))
            if asztal not in aktiv_rendelesek:
                print("[HIBA] Nincs aktív rendelés ennél az asztalnál!")
            else:
                if aktiv_rendelesek[asztal].lezar(vasarlasok):
                    del aktiv_rendelesek[asztal]

        elif valasztas == "5":
            print("\n--- ÉTLAP KEZELÉSE ---")
            print("1. Étlap listázása")
            print("2. Új étel hozzáadása")
            print("3. Étel törlése")
            sub = input("Válassz: ").strip()
            if sub == "1":
                etlap.listaz()
            elif sub == "2":
                nev = input("Étel neve: ").strip()
                ar = input("Étel ára: ").strip()
                etlap.hozzaad(nev, ar)
            elif sub == "3":
                nev = input("Törlendő étel neve: ").strip()
                etlap.torol(nev)
                receptek.torol(nev)

        elif valasztas == "6":
            raktarkeszlet.listaz()

        elif valasztas == "7":
            vasarlasok.listaz()

        elif valasztas == "0":
            print("Viszlát!")
            break

        else:
            print("[HIBA] Érvénytelen választás!")

main()