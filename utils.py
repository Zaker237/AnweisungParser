"""
    Authorin : Ramona Grosskopf
    Matrikulnummer: 788762
"""

import spacy
import re
# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

#nützliche Global Variable
DATA_NAME = "instructions.txt"
WORTERBUCH = {}
BIGRAMME_WORTERBUCH = {}

def lese_zeilen_in_data(path):
    """
        Diese Funktion wird dazu diennen die Zeile in einen Datei zu lesen.
        :param path: Das zu lesende Datei.
        :return: die Funtion gibt eine Liste zurrückt, die die Zeile des Data enthält.
    """

    file1 = open(path, 'r')
    #ich stelle mir hierbei sicher, dass ich nur die die nur die erste Sätze
    gab = [line[0:len(line)-1] for line in file1.readlines()]
    result = [anweisung.split(".")[0] for anweisung in gab]
    file1.close()
    return result

def replace_letter_with_nummer(anweisung):
    """
        Diese Funtion diennt dazu in einer Anweisung, die letter zur nummer zu umwandeln.
        :param anweisung: the Anweisung
        :return: die beiden index
    """
    result = anweisung
    for let in LETTER_TO_NUMBER.keys():
        if let in anweisung:
            result = result.replace(let, LETTER_TO_NUMBER[let], 1)
            return result
    return result

def finde_index_of_block(anweisung):
    """
        Diese Funtion diennt dazu in einer Anweisung, die Index von dem ZielBlock und dem Umgebungsblock
        zu finden:
        :param anweisung: the Anweisung
        :return: die beiden index
    """
    anweisung = replace_letter_with_nummer(anweisung)
    idxs = []
    word = ''
    index = 0
    for i in range(len(anweisung)):
        if anweisung[i] == '':
            if eval(word):
                idxs.append(index)
            word = ''
            index = i + 1
        else:
            word += anweisung[i]
    return idxs

def finde_index_of_nummer(anweisung):
    idxs = []
    for wort in anweisung.split(" "):
        if wort.isnumeric():
            idxs.append(anweisung.index(wort))
    return idxs

def tokennise_anweisungen(anweisung):
    """
        Diese function diennt dazu, die Tozen mit die Anweisungen zu generienden und
        dans Ihre Häufigkeit zu zählen.
        :param anweisungen: liste von anwiesungen
        :return: ein Dictionnaire, wo die keys die token und die value Ihre Häufigkeit.
    """
    doc = nlp(anweisung)
    result = [token.text for token in doc]
    return result

def parse_worterbuch(datei=DATA_NAME):
    """
        Diese function diennt dazu, die Token in der Corpus zu generieren und ihre 
        Häufigkeit zu zählen.
        :param anweisungen: der Datein Name
        :return: ein Dictionary, wo die token sind die Schlüssel, und ihre Häufigkeit sind die values
    """
    global WORTERBUCH
    worterbuch = {}
    anweisungen = lese_zeilen_in_data(datei)
    for anweisung in anweisungen:
       for wort in tokennise_anweisungen(anweisung):
            if wort in worterbuch:
                worterbuch[wort] += 1
            else:
                worterbuch[wort] = 1
    worterbuch =  dict(sorted(worterbuch.items(), key=lambda x: x[1], reverse=True))
    WORTERBUCH = worterbuch
    return worterbuch

def bigramme_zaelen(datei=DATA_NAME):
    """
        Diese function diennt dazu, die Bigramme in dem Corpus zu generienden und
        dans ihre Häufigkeit zu zählen.
        :param anweisungen: Der Datei Name
        :return: ein Dictionnaire, wo die keys die bigramme sind und die value ihre Häufigkeit.
    """
    global BIGRAMME_WORTERBUCH
    tokens = parse_worterbuch(datei)
    bigrame = []
    # wir machen aus den Token die Bigramme
    for token1 in tokens.keys():
        for token2 in tokens.keys():
            if token1 != token2:
                bigrame.append((token1,token2))
    
    result = {}
    texte = ". ".join(lese_zeilen_in_data(datei))
    for bi in bigrame:
        wort = bi[0]+' '+bi[1]
        bi_match = re.findall(re.escape(wort), texte)
        if len(bi_match) > 0:
            result[bi] = len(bi_match)
    
    result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
    BIGRAMME_WORTERBUCH = result
    return result

def finde_anweisung_mit_block(anweisung):
    """
        Diese function diennt dazu, Zielblock und Umgebungsblock in einer Anweisung zu finden,
        die das Wort Block enthält
        :param anweisungen: eine Anweisung
        :return: eine Liste von blöcke (Nummer die, das Wort Block folgen)
    """
    result = re.findall('block \d+', anweisung)
    return [re.findall(r'\d+', block)[0] for block in result]

def finde_anweisung_ohne_block(anweisung):
    """
        Diese function diennt dazu, Zielblock und Umgebungsblock in einer Anweisung zu finden,
        die kein Wort Block enthält
        :param anweisungen: eine Anweisung
        :return: eine Liste von blöcke (Nummer die, das Wort Block folgen)
    """
    result = re.findall('\d+', anweisung)
    return result

def replace_box_in_block(anweisung):
    """
        Diese function diennt dazu, das Wort box in einer Anweisung mit das Wort block zu ersetzen
        :param anweisungen: eine Anweisung
        :return: eine anweisung
    """
    result = anweisung.replace('box', 'block')
    return result

if __name__ == "__main__":
    print(f"die Liste von Anweisungen der Datei {DATA_NAME} : \n\n {lese_zeilen_in_data(DATA_NAME)}")
    print(f"die erste Anweisung is {lese_zeilen_in_data(DATA_NAME)[0]}")