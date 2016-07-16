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

    #SO TA VERIFICANDO RECURSAO ESQUERDA
    def recursao_esquerda(self):
        list_to_return  = []
        for nt, producao in self.producoes.items():
            if nt in producao[0]:
                split = producao[0].split('|')
                for forma_sentencial in split:
                    if nt in forma_sentencial:
                        list_to_return.append("%s -> %s" % (nt, forma_sentencial.strip()))
                        break
        return list_to_return

    def nd_direto(self):
        list_to_return = []
        for nao_terminal in self.producoes.keys():
            terminais = []
            for forma_sentencial in self.producoes[nao_terminal]:
                terminal = forma_sentencial[0]
                if terminal in terminais and nao_terminal not in list_to_return:
                    list_to_return.append(nao_terminal)
                if terminal in string.ascii_lowercase or terminal in string.digits:
                    terminais.append(terminal)

        print("ND Direto: ", list_to_return)
        return list_to_return

    def nd_indireto(self):
        list_to_return = []
        epsilon = False
        for nao_terminal in self.producoes.keys():
            simbolos = []
            for forma_sentencial in self.producoes[nao_terminal]:
                simbolo = forma_sentencial[0]
                if simbolo in string.ascii_lowercase or simbolo in string.digits:
                    simbolos.append(simbolo)
                elif simbolo in string.ascii_uppercase:
                    for f in self.get_first(simbolo):
                        if f != "&":
                            if f in simbolos and nao_terminal not in list_to_return:
                                list_to_return.append(nao_terminal)
                            simbolos.append(f)
                        elif f == "&":
                            epsilon = True
                    if epsilon:
                        i = 2
                        while len(forma_sentencial) >= i and epsilon:
                            if forma_sentencial[i] in string.ascii_lowercase or simbolo in string.digits:
                                if forma_sentencial[i] in simbolos and nao_terminal not in list_to_return:
                                    list_to_return.append(nao_terminal)
                                simbolos.append(forma_sentencial[i])
                            elif forma_sentencial[i] in string.ascii_uppercase:
                                for m in self.get_first(forma_sentencial[i]):
                                    if m != "&":
                                        if m in simbolos and nao_terminal not in list_to_return:
                                            list_to_return.append(nao_terminal)
                                        simbolos.append(m)
                                        epsilon = False
                                    elif m == "&":
                                        epsilon = True
                            i += 2

        print("Simbolos", simbolos)
        print("ND Indireto: ", list_to_return)
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
        if nao_terminal in string.ascii_lowercase:
            return nao_terminal
        first = []
        for forma_sentencial in self.producoes[nao_terminal]:
            # print("forma_sentencial:", forma_sentencial)
            for simbolo in forma_sentencial:
                if simbolo in string.ascii_lowercase or simbolo in string.digits or simbolo == "&":
                    if simbolo == forma_sentencial[0] and simbolo not in first:
                        first.append(simbolo)

        for forma_sentencial in self.producoes[nao_terminal]:
            cont = 0
            epsilon = 0
            if forma_sentencial[0] in string.ascii_uppercase and forma_sentencial[0] != nao_terminal:
                # print("forma_sentencial:", forma_sentencial)
                for m in self.get_first(forma_sentencial[0]):
                    if m in string.ascii_lowercase and m not in first:
                        first.append(m)
                i = 0
                while len(forma_sentencial) > i and forma_sentencial[i] in string.ascii_uppercase:
                    cont += 1
                    if forma_sentencial[i] != nao_terminal and "&" in self.get_first(forma_sentencial[i]):
                        epsilon += 1
                        if len(forma_sentencial) > i+2 and forma_sentencial[i+2] != nao_terminal:
                            if forma_sentencial[i+2] in string.ascii_lowercase:
                                cont = -1
                            for n in self.get_first(forma_sentencial[i+2]):
                                if n in string.ascii_lowercase and n not in first:
                                    first.append(n)
                    i += 2
                if cont == epsilon and "&" not in first:
                    first.append("&")
            # print(forma_sentencial, cont, epsilon)

        print("First de ", nao_terminal, first)
        return first

    def get_follow(self, nao_terminal):
        if nao_terminal not in self.producoes:
            return "###"
        follow = []
        epsilon = False
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
                                if n not in follow and n != "&":
                                    follow.append(n)
                                elif n == "&":
                                    epsilon = True
                            if epsilon:
                                for m in self.get_follow(aux):
                                    if m not in follow and m != "$":
                                        follow.append(m)
                                    elif m == "$" and len(producao) <= cont + 4 and "$" not in follow:
                                        follow.append("$")
                                epsilon = False
                    cont += 1
                cont = 0
        print("Follow de ", nao_terminal, follow)
        return follow

    def condicao3(self):
        for nao_terminal in self.producoes.keys():
            first_list = []
            for first in self.get_first(nao_terminal):
                first_list.append(first)
            for follow in self.get_follow(nao_terminal):
                if follow in first_list:
                    return False
        return True

    def is_LL1(self):
        if self.recursao_esquerda() != []:
            return False
        if self.nd_direto() != []:
            return False
        if self.nd_indireto() != []:
            return False
        if not self.condicao3():
            return False
        return True