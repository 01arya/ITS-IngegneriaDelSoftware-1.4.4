from voto import Voto
class Esame (Voto):
    '''
    def inizializzaVotoEsame(self,s):
        self.__Voto = Voto(0, s, self)
    '''
    def __init__(self,date,s,c):
        self.__data=date
        self.__studente=s
        self.__corso=c
        self.__superato="no"
        self.__voto=Voto(0,s,self)
        #self.inizializzaVotoEsame(self,s)

    def getData(self):
        return self.__data
    def getStudente(self):
        return self.__studente
    def getCorso(self):
        return self.__corso
    def getVoto(self):
        return self.__voto
    def getSuperato(self):
        return self.__superato

    def setData(self,d):
        self.__data=d
    def setStudente(self,s):
        self.__studente=s
    def setCorso(self,c):
        self.__corso=c
    def setSuperato(self,voto):
        if(voto>=18):
            self.__superato="si"
            self.getVoto().setVoto(voto)

