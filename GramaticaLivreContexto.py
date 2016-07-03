
class GramaticaLivreContexto:
    def __init__(self):
        self.producoes = {}

    def adiciona_producao(self, nao_terminal, forma_sentencial):
        if not nao_terminal in self.producoes:
            self.producoes[nao_terminal] = []
        if forma_sentencial in self.producoes[nao_terminal]: return False
        self.producoes[nao_terminal].append(forma_sentencial)
        return True
