Programmierprojekt : Parsen von einfachen Anweisungen
=====================================================

das Projekt wurde in 4 Datein aufgeteilt.

Datein
------

* Utils.py:

    diese Datein enthält nütztliche Funktionnen, die wir im programm brauchen wie zum Beispiel die Funktion **lese_zeilen_in_data** die diennt dazu die datei, wo die Anweisunggen sind zielweise zu lesen. alle Funktionnen in dieser Datein sind genug kommentiert.

* parse_anweisung.py:
    diese Datei enthält die Funktion zur Erzeugun von der CSV Datei mit die Anweisungen und ihre Zielbslock und Umgeburgsblocks

* RuleBasedParser.py:
    Diese data enthält die Deklaration der Klasse RuleBasedParser, die dazu diennt, eine Anweisung zu parsen. die Klasse hat genug Kommentare, die erklären, was die Attribute sind.

* main.py:
    diese Datei ist da um unsere programm zu starten. dans soll der benutzer  Datein name eingeben. eins wo die Anweisungen sind une der andere ist der name der CSV Datei

Wie Soll das Programm gestaret werden:
---------------------------------------
un das programm zu starten, soll die Datei **main.py** mit python ausgeführt werden. das kann im Kommandozeile mit dem Befehl **python main.py** gemacht werden. dannach muss man die Datein Name eingeben oder einfach Enter drücken für die defaut values nämlich intructions.txt für die Anweisung-Datei und geparste_anweisungen.csv für die CSV datein. Dann wird die CSV Datei erzeugt werden und darin könnte man sehen, für jeder Anweisung der Zielsblock und der Umgeburgslock(oder viel, wenn es mehrere gibt.)