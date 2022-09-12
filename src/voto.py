class Voto:
    def __init__(self,v,s,e):#esame
        self.__studente=s
        self.__esame=e
        if (v < 30 and v >= 0):
            self.__voto = v
        else:
            self.__voto = 0
    '''
    def __init__(self,v):#esame
        if (v < 30 and v >= 0):
            self.__voto = v
        else:
            self.__voto = 0
    '''
    def getVoto(self):#studente
        return self.__voto

    def setVoto(self,v):#docente
        if(v<30 and v>=0):
            self.__voto = v
            self.getStudente().addVoto(self.getVoto())

    def delVoto(self):
        self.__voto=0

    def getStudente(self):
        return self.__studente

    def setStudente(self,s):
        self.__studente=s

    def getEsame(self):
        return self.__esame

    def setEsame(self,e):
        self.__voto = e