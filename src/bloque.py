from datetime import datetime
from hashlib import sha256
from bson import json_util
import json

class Bloque:
    def __init__(self, index, cor, mot, hashArc, hashAnt, timestamp):
        self.index = index
        self.correo = cor
        self.motivo = mot
        self.hashArc = hashArc
        self.hashAnt = hashAnt
        self.timestamp = timestamp
        self.hashBloque = self.crearHash()

    def crearHash(self):
        hash = json.dumps(self.__dict__, sort_keys=True, default=json_util.default)
        return sha256(hash.encode()).hexdigest()