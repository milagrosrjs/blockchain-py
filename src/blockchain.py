from datetime import datetime
from hashlib import sha256
import json

class Bloque:
    def __init__(self, mail, razon, archivo, hashAnt, hashBlq, hashVer):
        self.mail = mail
        self.razon = razon
        self.archivo = archivo
        #self.tiempo = datetime.now()
        self.hashAnt = hashAnt
        self.hashBlq = hashBlq
        self.hashVer = hashVer

    def crearHash(self):
        hash = json.dumps(self.__dict__, sort_keys=True)
        return sha256(hash.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.cadena = []
        self.crearGenesis()

    def crearGenesis(self):
        bloqueGenesis = Bloque("", "", "", "0", "0", "0")
        bloqueGenesis.hashBlq = bloqueGenesis.crearHash()
        self.cadena.append(bloqueGenesis) 