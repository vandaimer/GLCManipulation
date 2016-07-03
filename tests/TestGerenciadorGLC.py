from GramaticaLivreContexto import GramaticaLivreContexto
from GerenciadorGLC import GerenciadorGLC
import unittest


class TestGerenciadorGLC(unittest.TestCase):
    def setUp(self):
        self.gglc = GerenciadorGLC()

    def test_retorna_true_se_adicionar_a_gramatica(self):
        glc = GramaticaLivreContexto()
        glc.adiciona_producao("S", "a")
        glc.adiciona_producao("A","A b")

        self.assertTrue(self.gglc.adicionar(glc))

    def test_retorna_numero_de_gramaticas_adicionadas(self):
        glc = GramaticaLivreContexto()
        glc.adiciona_producao("S", "a")
        glc.adiciona_producao("A","A b")

        self.gglc.adicionar(glc)
        self.assertEquals(len(self.gglc.gramaticas), 1)

    def test_retorna_numero_de_glc_apos_adicionar_duas_glc(self):
        glc = GramaticaLivreContexto()
        glc.adiciona_producao("S", "a")
        glc.adiciona_producao("A","A b")

        self.gglc.adicionar(glc)

        glc1 = GramaticaLivreContexto()
        glc1.adiciona_producao("S", "a")
        glc1.adiciona_producao("A","A b")

        self.assertTrue(len(self.gglc.gramaticas), 2)

    def test_retorna_false_se_glc_ja_foi_adicionada(self):
        glc = GramaticaLivreContexto()
        glc.adiciona_producao("S", "a")
        glc.adiciona_producao("A","A b")

        self.gglc.adicionar(glc)
        self.assertFalse(self.gglc.adicionar(glc))

    def test_retorna_true_se_adicionar_duas_glc_diferentes(self):
        glc = GramaticaLivreContexto()
        glc.adiciona_producao("S", "a")
        glc.adiciona_producao("A","A b")

        self.gglc.adicionar(glc)

        glc1 = GramaticaLivreContexto()
        glc1.adiciona_producao("S", "a")
        glc1.adiciona_producao("A","A b")

        self.assertTrue(self.gglc.adicionar(glc1))
