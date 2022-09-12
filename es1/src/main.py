# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from voto import *
from esame import *
from corso import *
from docente import *
from studente import *

def controlText(testo):
    if(len(testo)>20) or (len(testo)<2):
        raise(ValueError("Lunghezza del testo non accettabile"))
        return
    else:
        for x in testo:
            if(x>"z" or x<"A"):
                raise(ValueError("Il testo non può avere caratteri speciali"))
                return
def testText(testo,n):
    try:
        controlText(testo)
        print(f"test {n} passato")
    except ValueError as ve:
        print(f"errore test {n}:", ve.args)

def controlNumbers(n):
    if (len(n) > 20) or (len(n) < 1):
        raise (ValueError("Lunghezza del numero non è accettabile"))
        return
    else:
        for x in n:
            if (x.isdigit()):
                pass
            else:
                raise (ValueError("Il numero per essere tale non deve contenere caratteri diversi da cifre"))
                return

def testNumbers(n,t):
    try:
        controlNumbers(n)
        print(f"test {t} passato")
    except ValueError as ve:
        print(f"errore test {t}:", ve.args)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    testText("C@ao",1)
    testNumbers("1921a815",2)

    # studente
    s1=Studente("Mario","Rossi","19216811")
    print(f"studente:{s1.getMatricola()} {s1.getNome()} {s1.getCognome()}\n")
    '''
    s1.setNome("Veronica")
    print(f"studente:{s1.getMatricola()} {s1.getNome()} {s1.getCognome()}\n")
    '''

    # docente
    d1=Docente("Giacomo","Verdi")
    print(f"docente: {d1.getNome()} {d1.getCognome()}\n")

    #corso
    c1=Corso("Analisi1",d1)
    print(f"corso:\n\tnome corso:{c1.getNome()}\n\tdocente:{c1.getDoc().getNome()} {c1.getDoc().getCognome()}\n")

    #esame
    e1=Esame("08/09/2022",s1,c1)
    print(f"esame:\n\tnome corso:{e1.getCorso().getNome()}\n\tdocente:{e1.getCorso().getDoc().getNome()} {e1.getCorso().getDoc().getCognome()}\n\tstudente:{e1.getStudente().getMatricola()} {e1.getStudente().getNome()} {e1.getStudente().getCognome()}\n")

    #voto
    '''
    print('inserisci un voto:')
    v1=input()
    voto1=Voto(int(v1))
    print(f"voto:{voto1.getVoto()}\n")
    '''
    voto2=Voto(19,s1,e1)
    print(f"voto:{voto2.getVoto()}\n\tesame:\n\t\tnome corso:{voto2.getEsame().getCorso().getNome()}\n\t\tdocente:{voto2.getEsame().getCorso().getDoc().getNome()} {voto2.getEsame().getCorso().getDoc().getCognome()}\n\tstudente:{voto2.getStudente().getMatricola()} {voto2.getStudente().getNome()} {voto2.getStudente().getCognome()}")
    voto2.getEsame().setSuperato(voto2.getVoto())
    print(f"\tesame superato? {voto2.getEsame().getSuperato()}")

    #INTEGRAZIONE


    s1.iscrizioneCorso(c1.getNome())#devo mettere l'oggetto non il nome del corso
    print(f"lista corsi studente: {s1.getCorsi()}")

    s1.iscrizioneEsame(e1)
    print(f"lista esami studente:{s1.getEsami()}")

    print(f"lista voti studente:{s1.getVoti()}")  # automatico con l'inseriemnto dell'voto

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
