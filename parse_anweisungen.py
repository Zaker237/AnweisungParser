"""
    Authorin : Ramona Grosskopf
    Matrikulnummer: 788762
"""

import csv
import os
from utils import lese_zeilen_in_data
from RuleBasedParser import RuleBasedParser

def create_csv_mit_daten(anweisungen = "instructions.txt", datei_namen = "instructions.csv",):
    """
        diese Funktion dient dazu die CSV data zu erzeugen.
        :param datei_name: der Name der zu erzeugende CSV Datei
        :param anweisung_liste: die liste von Anweisung, die wir in der Datei geschrieben werden soll. 
    """
    anweisung_liste = lese_zeilen_in_data(anweisungen)
    with open(datei_namen, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["Anweisung", "Zielsblock", "Umgebungsblock"])
        for anweisung in anweisung_liste:
            parser = RuleBasedParser(anweisung)
            spamwriter.writerow([parser.anweisung, parser.zielsblock, '#'.join(parser.umgeburgsblocks)])


if __name__ == "__main__":
    DATA_NAME = "instructions.txt"
    CSV_DATA_NAME = "instructions.csv"
    create_csv_mit_daten(lese_zeilen_in_data(DATA_NAME), CSV_DATA_NAME)
    
