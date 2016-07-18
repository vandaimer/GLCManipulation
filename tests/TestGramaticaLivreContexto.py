from GramaticaLivreContexto import GramaticaLivreContexto
import unittest

class TestGramaticaLivreContexto(unittest.TestCase):
    def setUp(self):
        self.glc = GramaticaLivreContexto()

    def test_retorna_true_se_adiciona_a_prod(self):
        self.assertTrue(self.glc.adiciona_producao("S", "a S"))

    def test_verifica_numero_de_producoes_apos_adicionar_1_prod(self):
        self.glc.adiciona_producao("S", "a S")
        self.assertEqual(len(self.glc.producoes), 1)

    def test_verifica_numero_de_producoes_apos_adicionar_a_segunda_prod_com_mesmo_NT(self):
        self.glc.adiciona_producao("S", "a S")
        self.glc.adiciona_producao("S", "b A")

        self.assertEqual(len(self.glc.producoes["S"]), 2)

    def test_verifica_numero_de_producoes_apos_adicionar_a_segunda_prod(self):
        self.glc.adiciona_producao("S", "a S")
        self.glc.adiciona_producao("A", "b A")
        self.assertEqual(len(self.glc.producoes), 2)

    def test_retorna_false_se_a_producao_ja_foi_adiciona_com_um_dado_NT(self):
        self.glc.adiciona_producao("S", "a S")
        self.assertFalse(self.glc.adiciona_producao("S", "a S"))

    def test_first(self):
        # self.glc.adiciona_producao("S", "A B C")
        # self.glc.adiciona_producao("A", "a A")
        # self.glc.adiciona_producao("A", "a")
        # self.glc.adiciona_producao("A", "&")
        #
        # self.glc.adiciona_producao("B", "b")
        # self.glc.adiciona_producao("B", "&")
        #
        # self.glc.adiciona_producao("C", "c")
        # self.glc.adiciona_producao("C", "&")

        # self.glc.adiciona_producao("S", "A B C")
        #
        # self.glc.adiciona_producao("A", "a A")
        # self.glc.adiciona_producao("A", "&")
        #
        # self.glc.adiciona_producao("B", "b B")
        # self.glc.adiciona_producao("B", "A C d")
        #
        # self.glc.adiciona_producao("C", "c C")
        # self.glc.adiciona_producao("C", "&")

        self.glc.adiciona_producao("S", "A b C D")
        self.glc.adiciona_producao("S", "E F")
        self.glc.adiciona_producao("A", "a A")
        self.glc.adiciona_producao("A", "&")
        self.glc.adiciona_producao("C", "E C F")
        self.glc.adiciona_producao("C", "c")
        self.glc.adiciona_producao("D", "C D")
        self.glc.adiciona_producao("D", "d D d")
        self.glc.adiciona_producao("D", "&")
        self.glc.adiciona_producao("E", "e E")
        self.glc.adiciona_producao("E", "&")
        self.glc.adiciona_producao("F", "F S")
        self.glc.adiciona_producao("F", "f F")
        self.glc.adiciona_producao("F", "g")

        self.glc.get_first("S")

    def test_follow(self):
        # self.glc.adiciona_producao("S", "A b C")
        # self.glc.adiciona_producao("A", "a A")
        # self.glc.adiciona_producao("A", "a")
        # self.glc.adiciona_producao("C", "c C")
        # self.glc.adiciona_producao("C", "c")

        # self.glc.adiciona_producao("S", "A B C")
        # self.glc.adiciona_producao("A", "a A")
        # self.glc.adiciona_producao("A", "&")
        # self.glc.adiciona_producao("B", "b B")
        # self.glc.adiciona_producao("B", "A C d")
        # self.glc.adiciona_producao("C", "c C")
        # self.glc.adiciona_producao("C", "&")

        self.glc.adiciona_producao("S", "A b C D")
        self.glc.adiciona_producao("S", "E F")
        self.glc.adiciona_producao("A", "a A")
        self.glc.adiciona_producao("A", "&")
        self.glc.adiciona_producao("C", "E C F")
        self.glc.adiciona_producao("C", "c")
        self.glc.adiciona_producao("D", "C D")
        self.glc.adiciona_producao("D", "d D d")
        self.glc.adiciona_producao("D", "&")
        self.glc.adiciona_producao("E", "e E")
        self.glc.adiciona_producao("E", "&")
        self.glc.adiciona_producao("F", "F S")
        self.glc.adiciona_producao("F", "f F")
        self.glc.adiciona_producao("F", "g")

        self.glc.get_follow("C")

    def test_nd_direto(self):
        # self.glc.adiciona_producao("S", "A b C")
        # self.glc.adiciona_producao("A", "a A")
        # self.glc.adiciona_producao("A", "a")
        # self.glc.adiciona_producao("C", "c C")
        # self.glc.adiciona_producao("C", "c")

        # self.glc.adiciona_producao("S", "A B C")
        # self.glc.adiciona_producao("A", "a A")
        # self.glc.adiciona_producao("A", "&")
        # self.glc.adiciona_producao("B", "b B")
        # self.glc.adiciona_producao("B", "A C d")
        # self.glc.adiciona_producao("C", "c C")
        # self.glc.adiciona_producao("C", "&")

        self.glc.adiciona_producao("S", "A b C D")
        self.glc.adiciona_producao("S", "E F")
        self.glc.adiciona_producao("A", "a A")
        self.glc.adiciona_producao("A", "a C")
        self.glc.adiciona_producao("A", "a D")
        self.glc.adiciona_producao("A", "&")
        self.glc.adiciona_producao("C", "E C F")
        self.glc.adiciona_producao("C", "c")
        self.glc.adiciona_producao("D", "C D")
        self.glc.adiciona_producao("D", "d D d")
        self.glc.adiciona_producao("D", "&")
        self.glc.adiciona_producao("E", "e E")
        self.glc.adiciona_producao("E", "&")
        self.glc.adiciona_producao("F", "F S")
        self.glc.adiciona_producao("F", "f F")
        self.glc.adiciona_producao("F", "g")

        self.glc.nd_direto()

    def test_nd_indireto(self):
        # self.glc.adiciona_producao("S", "A b C")
        # self.glc.adiciona_producao("A", "a A")
        # self.glc.adiciona_producao("A", "a")
        # self.glc.adiciona_producao("C", "c C")
        # self.glc.adiciona_producao("C", "c")

        # self.glc.adiciona_producao("S", "A B C")
        # self.glc.adiciona_producao("A", "a A")
        # self.glc.adiciona_producao("A", "&")
        # self.glc.adiciona_producao("B", "b B")
        # self.glc.adiciona_producao("B", "A C d")
        # self.glc.adiciona_producao("C", "c C")
        # self.glc.adiciona_producao("C", "&")

        self.glc.adiciona_producao("S", "A b C D | E F")
        # self.glc.adiciona_producao("S", "E F")
        self.glc.adiciona_producao("A", "a A")
        self.glc.adiciona_producao("A", "a C")
        self.glc.adiciona_producao("A", "a D")
        self.glc.adiciona_producao("A", "&")
        self.glc.adiciona_producao("C", "E C F")
        self.glc.adiciona_producao("C", "c")
        self.glc.adiciona_producao("D", "C D")
        self.glc.adiciona_producao("D", "d D d")
        self.glc.adiciona_producao("D", "&")
        self.glc.adiciona_producao("E", "a E")
        self.glc.adiciona_producao("E", "e E")
        self.glc.adiciona_producao("E", "&")
        self.glc.adiciona_producao("F", "F S")
        self.glc.adiciona_producao("F", "f F")
        self.glc.adiciona_producao("F", "g")

        self.glc.nd_indireto()

    def test_condicao_3(self):
        self.glc.adiciona_producao("S", "A b C D")
        self.glc.adiciona_producao("S", "E F")
        self.glc.adiciona_producao("A", "a A")
        self.glc.adiciona_producao("A", "a C")
        self.glc.adiciona_producao("A", "a D")
        self.glc.adiciona_producao("A", "&")
        self.glc.adiciona_producao("C", "E C F")
        self.glc.adiciona_producao("C", "c")
        self.glc.adiciona_producao("D", "C D")
        self.glc.adiciona_producao("D", "d D d")
        self.glc.adiciona_producao("D", "&")
        self.glc.adiciona_producao("E", "a E")
        self.glc.adiciona_producao("E", "e E")
        self.glc.adiciona_producao("E", "&")
        self.glc.adiciona_producao("F", "F S")
        self.glc.adiciona_producao("F", "f F")
        self.glc.adiciona_producao("F", "g")

        # self.glc.adiciona_producao("S", "A b C")
        # self.glc.adiciona_producao("A", "a A")
        # self.glc.adiciona_producao("A", "a")
        # self.glc.adiciona_producao("C", "c C")
        # self.glc.adiciona_producao("C", "c")

        # self.glc.get_first("C")
        # self.glc.get_follow("C")
        self.assertFalse(self.glc.condicao3())

    def test_is_LL1(self):
        self.glc.adiciona_producao("S", "A b C D")
        self.glc.adiciona_producao("S", "E F")
        self.glc.adiciona_producao("A", "a A")
        self.glc.adiciona_producao("A", "a C")
        self.glc.adiciona_producao("A", "a D")
        self.glc.adiciona_producao("A", "&")
        self.glc.adiciona_producao("C", "E C F")
        self.glc.adiciona_producao("C", "c")
        self.glc.adiciona_producao("D", "C D")
        self.glc.adiciona_producao("D", "d D d")
        self.glc.adiciona_producao("D", "&")
        self.glc.adiciona_producao("E", "a E")
        self.glc.adiciona_producao("E", "e E")
        self.glc.adiciona_producao("E", "&")
        self.glc.adiciona_producao("F", "F S")
        self.glc.adiciona_producao("F", "f F")
        self.glc.adiciona_producao("F", "g")

        # self.glc.get_first("C")
        # self.glc.get_follow("C")
        self.assertFalse(self.glc.is_LL1())

    def test_TP(self):
        # self.glc.adiciona_producao("S", "A b C D")
        # self.glc.adiciona_producao("S", "E F")
        # self.glc.adiciona_producao("A", "a A")
        # self.glc.adiciona_producao("A", "a C")
        # self.glc.adiciona_producao("A", "a D")
        # self.glc.adiciona_producao("A", "&")
        # self.glc.adiciona_producao("C", "E C F")
        # self.glc.adiciona_producao("C", "c")
        # self.glc.adiciona_producao("D", "C D")
        # self.glc.adiciona_producao("D", "d D d")
        # self.glc.adiciona_producao("D", "&")
        # self.glc.adiciona_producao("E", "a E")
        # self.glc.adiciona_producao("E", "e E")
        # self.glc.adiciona_producao("E", "&")
        # self.glc.adiciona_producao("F", "F S")
        # self.glc.adiciona_producao("F", "f F")
        # self.glc.adiciona_producao("F", "g")

        self.glc.adiciona_producao("S", "A b C")
        self.glc.adiciona_producao("A", "a")
        self.glc.adiciona_producao("C", "c")

        self.glc.TP()

    def test_Parser(self):
        self.glc.adiciona_producao("S", "A b C")
        self.glc.adiciona_producao("A", "&")
        self.glc.adiciona_producao("A", "a")
        self.glc.adiciona_producao("C", "c")

        self.glc.parser()