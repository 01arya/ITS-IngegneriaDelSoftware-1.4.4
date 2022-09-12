class Studente:
    def __init__(self,n,c,id):
        self.__matricola=id
        self.__nome=n
        self.__cognome=c
        self.__corsi=[]
        self.__esami=[]
        self.__voti=[]

    def getNome(self):
        return self.__nome

    def getCognome(self):
        return self.__cognome

    def getMatricola(self):
        return self.__matricola

    def getCorsi(self):
        return self.__corsi

    def getEsami(self):
        return self.__esami

    def setNome(self,n):
        self.__nome=n

    def setCognome(self,c):
        self.__cognome=c

    def setMatricola(self,m):
        self.__matricola=m

    def iscrizioneCorso(self,c):
        if c not in self.__corsi:
            self.__corsi.append(c)

    def iscrizioneEsame(self,e):
        if e not in self.__esami:
            if e.getCorso in self.getCorsi():
                self.__esami.append(e)

    def corsiDisponibili(self,l):
        for c in l not in self.__corsi:
            print(c)

    def getVoti(self):
        return self.__voti

    def addVoto(self,v):
        self.__voti.append(v)


