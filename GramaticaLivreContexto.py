import string

class GramaticaLivreContexto:
    def __init__(self):
        self.producoes = {}

    def adiciona_producao(self, nao_terminal, forma_sentencial):
        if not nao_terminal in self.producoes:
            self.producoes[nao_terminal] = []
        if forma_sentencial in self.producoes[nao_terminal]: return False
        self.producoes[nao_terminal].append(forma_sentencial)
        return True

    def get_first(self, nao_terminal):
        if nao_terminal not in self.producoes:
            return False
        first = []
        for forma_sentencial in self.producoes[nao_terminal]:
            for simbolo in forma_sentencial:
                if simbolo in string.ascii_lowercase or simbolo in string.digits:
                    if simbolo == forma_sentencial[0] and simbolo not in first:
                        first.append(simbolo)
                elif simbolo in string.ascii_uppercase and simbolo == forma_sentencial[0]:
                    for n in self.get_first(simbolo):
                        if n not in first:
                            first.append(n)

        return first

