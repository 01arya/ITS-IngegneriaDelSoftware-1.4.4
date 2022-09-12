class Corso:
    def __init__(self,nome,docente):
        self.__nome=nome
        self.__docente=docente
        self.__studenti=[]
        self.__esami=[]

    def getNome(self):
        return self.__nome
    def getDoc(self):
        return self.__docente
    def setNome(self,nome):
        self.__nome = nome
    def setDoc(self,docente):
        self.__docente = docente

    def setStudenti(self,studenti):
        self.__studenti=studenti

    def getStudenti(self):
        return self.__studenti

    def insertStudente(self,studente):
        self.__studenti.append(studente)

    def setEsami(self, esami):
        self.__esami = esami

    def getEsami(self):
        return self.__esami

    def insertEsame(self, esame):
        self.__esami.append(esame)