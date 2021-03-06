import os
import sys
import json
from bson import json_util
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from src.singleton import Singleton
from src.bloque import Bloque
from datetime import datetime

class Blockchain(metaclass=Singleton): #clase blockchain con singleton
    def __init__(self):
        self.__cadena = [] #almacena los bloques de la blockchain
        self.__zero_count = 0 #Cambiar complejidad
        self.__crearGenesis()
        
    def __crearGenesis(self): #crea bloque genesis con los atributos de Bloque
        bloqueGenesis = Bloque(0, "", "", "0", "0", "2021-01-01 00:00:00", self.__zero_count)
        self.__cadena.append(bloqueGenesis)
    
    def __crearBloque(self, cor, mot, hashArc, timestamp):
        newBloque = Bloque(self.__getNextBloqueIndex(), cor, mot, hashArc, self.__getPreviusBloqueHash(), timestamp, self.__zero_count)
        self.__cadena.append(newBloque)

    def __getNextBloqueIndex(self): #devuelve el id de bloque
        return len(self.__cadena)

    def __getPreviusBloqueHash(self):
        return self.getHashByIndex(self.__getNextBloqueIndex() - 1)

    def crearBloque(self, cor, mot, hashArc):
        newBloque = Bloque(self.__getNextBloqueIndex(), cor, mot, hashArc, self.__getPreviusBloqueHash(),datetime.now().strftime("%Y-%m-%d %H:%M:%S"), self.__zero_count)
        self.__cadena.append(newBloque)

    def getHashByIndex(self, index):
        return self.__cadena[index].hashBloque
    
    def getBloqueByIndex(self, index):
        return self.__cadena[index]
    
    def getJsonBloqueByIndex(self, index):
        bloque = self.__cadena[index]
        return json.dumps(bloque.__dict__, sort_keys=True, default=json_util.default)

    def setZero_count(self, count):
        self.__zero_count = count

    def getBlockByHash(self, hash):
        for bloque in self.__cadena:
            if hash == bloque.hashBloque:
                return bloque
        
    def comprueba(self):
        hash = '0'
        for bloque in self.__cadena:
            if bloque.hashAnt == hash:
                hash = bloque.hashBloque
            else:
                return False
        if self.lastBlock().hashBloque == hash:
            return True
        else:
            return False
    
    def lastBlock(self):
        return self.__cadena[-1]
