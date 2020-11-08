"""
    Author: Alex Mboutchouang
    Email: mboutchouangalex@gmail.com
    Repository:  https://github.com/Zaker237/AnweisungParser.git
"""

from parse_anweisungen import create_csv_mit_daten


if __name__ == "__main__":
    inst_data_name = input("Gebe bitte ein die name des Datei ein, das Anweisungen enthält \n or Enter für instructions.txt: ") or "instructions.txt"
    csv_data_name = input("Gebe bitte ein die name der CSV Datei ein: ") or "geparste_anweisungen.csv"
    try:
        create_csv_mit_daten(inst_data_name, csv_data_name)
        print(f"das Datei {csv_data_name} wurde erfolgreich erstellt.")
    except:
        print("Starten Sie neue und geben sie Bitte richtigen Datei Namen")
