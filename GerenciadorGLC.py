import pickle
import os

class GerenciadorGLC:
    def __init__(self, filename="dump_glc"):
        self.filename = filename
        self.gramaticas = []
        self.carregar()

    def adicionar(self, glc):
        if self.gramaticas.count(glc) > 0: return False
        self.gramaticas.append(glc)
        return True

    def obtem_by_index(self, index):
        try:
            return self.gramaticas[index]
        except Exception as e:
            return False

    def remover_by_index(self, index):
        try:
            del self.gramaticas[index]
            return True
        except Exception as e:
            return False

    def salvar(self):
        try:
            pickle.dump(self.gramaticas, open(self.filename, 'wb'))
            return True
        except Exception as e:
            return False

    def carregar(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            glcs_carregadas = pickle.load(open(self.filename, 'rb'))
            for glc in glcs_carregadas:
                self.gramaticas.append(glc)
