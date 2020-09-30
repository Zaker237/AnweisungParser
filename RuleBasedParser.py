"""
    Authorin : Ramona Grosskopf
    Matrikulnummer: 788762
"""

from utils import finde_anweisung_mit_block, finde_anweisung_ohne_block, replace_box_in_block
import spacy

class RuleBasedParser():
    def __init__(self, anweisung):
        """
            Die Klasse diennt dazu eine Anweisung zu parsen.
            :param anweisungen: die Anweisung, die die Klasse zu parsen soll.
            :attribute anweisung: die Anweisung.
            :attribute zielsblock: der Zielsblock, der in der Anweisung gefunden wurde.
            :attribute umgeburgsblocks: die Liste auf umgeburgsblöcke, die in der Anweisung gefunden wurden.
            :attribute nlp: die English language model(damit initialisieren wir spacy, um später damit die Anweisung zu verstehen).
            :attribute doc: die liste auf tokens in der Anweisung.
            :method parse: die funktion zum parsen der Anweisung.
        """
        #wenn das Wort 'box' in der Anweisung auftritt, den mit 'block ersetzen'
        self.anweisung = replace_box_in_block(anweisung) 
        self.zielsblock = ''
        self.umgeburgsblocks = []
        self.nlp = spacy.load("en_core_web_sm")
        self.doc = self.nlp(anweisung)

        #wir parsen die Anweisung 
        self.parse()
    
    def parse(self):
        """
            Diese function diennt dazu, eine Anweisung zu Parsen.
            :param anweisungen: eine Anweisung
            :return: ein tupel, wo der erste element der Zielblock ist und die 2 eine liste von Umgebungsblöcke ist.
        """

        #Falle wo alle blöcke sind mit das Wort blog bezeichet:
        if len(finde_anweisung_mit_block(self.anweisung)) >= 2:
            result = finde_anweisung_mit_block(self.anweisung)
            self.zielsblock = result[0]
            self.umgeburgsblocks =  result[1:]
        elif len(finde_anweisung_mit_block(self.anweisung)) == 1:
            #Falle wo block nur eimal in der Anweisung vorkommt
            pass
        else:
            #Fall block(oder box) gar nicht in der Anweisung vorkommt
            if len(finde_anweisung_ohne_block(self.anweisung)) >=2:
                #Falle wo alle blöcke sind ohne das Wort block geschrieben:
                result = finde_anweisung_ohne_block(self.anweisung)
                self.zielsblock = result[0]
                self.umgeburgsblocks =  result[1:]
            elif len(finde_anweisung_ohne_block(self.anweisung)) ==1:
                #fall wo nur im Nummer auftritt in der Anweisung
                pass
            else:
                #Falls wo all in text geschrieben ist
                for token in self.doc:
                    if token.is_digit:
                        pass


if __name__ == "__main__":
    anw1 = "Move 8 so it is above 9"
    parser1 = RuleBasedParser(anw1)
    print(f"Anwaidung: {parser1.anweisung}, \n Zielsblock: {parser1.zielsblock}, \n Umgebungsblocks: {parser1.umgeburgsblocks}")

    anw2 = "Move block 7 to the left of block 12."
    parser2 = RuleBasedParser(anw2)
    print(f"Anwaidung: {parser2.anweisung}, \n Zielsblock: {parser2.zielsblock}, \n Umgebungsblocks: {parser2.umgeburgsblocks}")

    anw3 = "Find box 14 in the bottom left corner. Move it so that it lines up in the corner created by boxes 10 and 15 on the right side of the mat."
    parser3 = RuleBasedParser(anw3)
    print(f"Anwaidung: {parser3.anweisung}, \n Zielsblock: {parser3.zielsblock}, \n Umgebungsblocks: {parser3.umgeburgsblocks}")
