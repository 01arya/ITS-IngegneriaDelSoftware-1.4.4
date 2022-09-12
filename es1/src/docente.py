class Docente:
    def __init__(self,n,c):
        self.__nome=n
        self.__cognome=c
        self.__insegnamenti=[]

    def getNome(self):
        return self.__nome

    def getCognome(self):
        return self.__cognome

    def setNome(self,n):
        self.__nome=n

    def setCognome(self,c):
        self.__cognome=c

    def aggiungiInsegnamento(self, c):
        self.__insegnamenti.append(c)

    def iscrizioneEsame(self, e):
        self.__esami.append(e)