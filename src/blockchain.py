from src.bloque import Bloque
from datetime import datetime

class Blockchain:
    def __init__(self):
        self.cadena = []
        self.crearGenesis()

    def crearGenesis(self):
        bloqueGenesis = Bloque(0, "", "", "0", "0", "2021-01-01 00:00:00")
        self.cadena.append(bloqueGenesis)
    
    def crearBloque(self, cor, mot, hashArc):
        newBloque = Bloque(self.getNextBloqueIndex(), cor, mot, hashArc, self.getPreviusBloqueHash(), "2021-01-01 22:00:00")
        self.cadena.append(newBloque)

    def getNextBloqueIndex(self):
        return len(self.cadena)

    def getPreviusBloqueHash(self):
        return self.getHashByIndex(self.getNextBloqueIndex() - 1)

    def getDateTimeString(self): 
        datatime = datetime.now()
        return datatime.isoformat()

    def getFormatDate(self, timestamp):
        return datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')

    def getHashByIndex(self, index):
        return self.cadena[index].hashBloque