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
        self.glc.adiciona_producao("S", "A b C")
        self.glc.adiciona_producao("A", "a A")
        self.glc.adiciona_producao("A", "a")
        self.glc.adiciona_producao("C", "c C")
        self.glc.adiciona_producao("C", "c")
        self.glc.get_first("C")

    def test_follow(self):
        self.glc.adiciona_producao("S", "A b C")
        self.glc.adiciona_producao("A", "a A")
        self.glc.adiciona_producao("A", "a")
        self.glc.adiciona_producao("C", "c C")
        self.glc.adiciona_producao("C", "c")
        self.glc.get_follow("S")
