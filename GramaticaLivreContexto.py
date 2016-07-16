import string
import re

class GramaticaLivreContexto:
    def __init__(self):
        self.producoes = {}
        self.inicial = ""

    def adiciona_producao(self, nao_terminal, forma_sentencial):
        if not nao_terminal in self.producoes:
            self.producoes[nao_terminal] = []
            if self.inicial == "":
                self.inicial = nao_terminal
        if forma_sentencial in self.producoes[nao_terminal]: return False
        self.producoes[nao_terminal].append(forma_sentencial)
        return True

    #SO TA VERIFICANDO RECURSAO ESQUERDA DIRETA
    def recursao_esquerda_direta(self):
        list_to_return = []
        for nao_terminal in self.producoes.keys():
            lista_nao_terminais = self._recursao_esquerda_direta(nao_terminal)
            if len(lista_nao_terminais):
                list_to_return.append(lista_nao_terminais)
        return list_to_return

    def recursao_esquerda_indireta(self):
        list_to_return = []
        for nao_terminal in self.producoes.keys():
            lista_nao_terminais = self._recursao_esquerda_indireta(nao_terminal)
            if len(lista_nao_terminais):
                list_to_return.append(lista_nao_terminais)
        return list_to_return

    def _recursao_esquerda_direta(self, n_terminal):
        producoes = self.producoes[n_terminal][0]
        lista_producoes = producoes.split('|')
        list_to_return  = []
        for producao in lista_producoes:
            if n_terminal == producao.strip()[0]:
                list_to_return.append(n_terminal)
                break
        return list_to_return

    def _recursao_esquerda_indireta(self, n_terminal):
        producoes = self.producoes[n_terminal][0]
        lista_nao_terminais = self._obtem_nao_terminais_esquerda(n_terminal)
        list_to_return  = []
        for x in lista_nao_terminais:
            if x in self.producoes:
                producoes = self.producoes[x][0]
                lista_producoes = producoes.split('|')
                for producao in lista_producoes:
                    if n_terminal == producao.strip()[0]:
                        list_to_return.append(x)
                        break
        return list_to_return

    def _obtem_nao_terminais_esquerda(self, n_terminal):
        producoes = self.producoes[n_terminal][0]
        lista_producoes = producoes.split('|')
        list_to_return  = []
        for producao in lista_producoes:
            primeiro_simbolo = producao.strip()[0]
            if producao.strip()[0].isupper() and primeiro_simbolo != n_terminal:
                list_to_return.append(primeiro_simbolo)
        return list_to_return

    def get_all_first(self):
        dict_first = {}
        for nao_terminal in self.producoes.keys():
            dict_first[nao_terminal] = self.get_first(nao_terminal)

        return dict_first

    def get_all_follow(self):
        dict_follows = {}
        for nao_terminal in self.producoes.keys():
            dict_follows[nao_terminal] = self.get_follow(nao_terminal)

        return dict_follows

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

    def get_follow(self, nao_terminal):
        if nao_terminal not in self.producoes:
            return False
        follow = []
        cont = 0
        if nao_terminal == self.inicial:
            follow.append("$")
        for forma_sentencial in self.producoes:
            for producao in self.producoes[forma_sentencial]:
                for simbolo in producao:
                    if simbolo == nao_terminal:
                        aux = "###"
                        if cont + 2 < len(producao):
                            aux = producao[cont+2]
                        elif forma_sentencial == self.inicial and "$" not in follow:
                            follow.append("$")
                        if aux in string.ascii_lowercase or aux in string.digits:
                            if aux not in follow:
                                follow.append(aux)
                        elif aux in string.ascii_uppercase:
                            for n in self.get_first(aux):
                                follow.append(n)
                    cont += 1
                cont = 0
        return follow
