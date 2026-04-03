def beolvas(fajlnev):
    adatok = []
    try:
        with open(fajlnev, "r", encoding="utf-8") as f:
            for sor in f:
                sor = sor.strip()
                if sor:
                    mezok = [mezo.strip() for mezo in sor.split(";")]
                    adatok.append(mezok)
    except FileNotFoundError:
        print(f"[HIBA] A '{fajlnev}' fájl nem található.")
    return adatok


def kiment(fajlnev, adatok):
    with open(fajlnev, "w", encoding="utf-8") as f:
        for sor in adatok:
            szoveg = ";".join(str(x) for x in sor)
            f.write(szoveg + "\n")