from datetime import datetime
from hashlib import sha256
import json

class Bloque:
    def __init__(self, index, mail, razon, hashArchivo, hashAnt):
        self.index = index
        self.mail = mail
        self.razon = razon
        self.hashArchivo = hashArchivo
        #self.tiempo = datetime.now()
        self.hashAnt = hashAnt
        self.hashBlq = self.crearHash()
        

    def crearHash(self):
        hash = json.dumps(self.__dict__, sort_keys=True)
        return sha256(hash.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.cadena = []
        self.crearGenesis()

    def crearGenesis(self):
        bloqueGenesis = Bloque(0, "", "", "0", "0")
        self.cadena.append(bloqueGenesis) 

    def crearBloque(self):
        pass

    def getHashByIndex(self, index):
        return self.cadena[index].hashBlq