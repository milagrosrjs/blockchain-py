import os
import sys
import json
from bson import json_util
from singleton import Singleton
from bloque import Bloque
from datetime import datetime

class Blockchain(metaclass=Singleton):
    def __init__(self):
        self.__cadena = []
        self.__zero_count = 0
        self.__crearGenesis()
        
    def __crearGenesis(self):
        bloqueGenesis = Bloque(0, "", "", "0", "0", "2021-01-01 00:00:00", self.__zero_count)
        self.__cadena.append(bloqueGenesis)
    
    def __crearBloque(self, cor, mot, hashArc, timestamp):
        newBloque = Bloque(self.__getNextBloqueIndex(), cor, mot, hashArc, self.__getPreviusBloqueHash(), timestamp, self.__zero_count)
        self.__cadena.append(newBloque)

    def __getNextBloqueIndex(self):
        return len(self.__cadena)

    def __getPreviusBloqueHash(self):
        return self.getHashByIndex(self.__getNextBloqueIndex() - 1)

    def crearBloque(self, cor, mot, hashArc):
        newBloque = Bloque(self.__getNextBloqueIndex(), cor, mot, hashArc, self.__getPreviusBloqueHash(), datetime.utcnow, self.__zero_count)
        self.__cadena.append(newBloque)

    def getHashByIndex(self, index):
        return self.__cadena[index].hashBloque
    
    def getBloqueByIndex(self, index):
        return self.__cadena[index]
    
    def getJsonBloqueByIndex(self, index):
        return json.dumps(self.__cadena[index], sort_keys=True, default=json_util.default)

    def setZero_count(self, count):
        self.__zero_count = count

    def getBlockByHash(self, hash):
        for bloque in self.__cadena:
            if hash == bloque.hashBloque:
                return bloque
        return 'none'