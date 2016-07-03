

class GerenciadorGLC:
    def __init__(self):
        self.gramaticas = []

    def adicionar(self, glc):
        if self.gramaticas.count(glc) > 0: return False
        self.gramaticas.append(glc)
        return True
