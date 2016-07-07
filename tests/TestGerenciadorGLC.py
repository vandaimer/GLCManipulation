from GramaticaLivreContexto import GramaticaLivreContexto
from GerenciadorGLC import GerenciadorGLC
import unittest
import os


class TestGerenciadorGLC(unittest.TestCase):

    def setUp(self):
        self.dump = 'test_dump_gramaticas'
        self.gglc = GerenciadorGLC(self.dump)

    def tearDown(self):
        if os.path.exists(self.dump):
            os.remove(self.dump)

    def test_salva_em_arquivo_as_glcs(self):
        glc = GramaticaLivreContexto()
        glc.adiciona_producao("S", "a")
        glc.adiciona_producao("A","A b")
        self.gglc.adicionar(glc)

        self.assertTrue(self.gglc.salvar())

    def test_salva_e_carrega_uma_glc_do_arquivo(self):
        glc = GramaticaLivreContexto()
        glc.adiciona_producao("S", "a")
        glc.adiciona_producao("A","A b")
        self.gglc.adicionar(glc)
        self.gglc.salvar()

        self.gglc.gramaticas = []
        self.gglc.carregar()
        self.assertEquals(len(self.gglc.gramaticas), 1)

    def test_merge_de_glc_ao_carregar_e_add_a_mesma_glc(self):
        glc = GramaticaLivreContexto()
        glc.adiciona_producao("S", "a")
        glc.adiciona_producao("A","A b")

        self.gglc.adicionar(glc)
        self.gglc.salvar()
        self.gglc.carregar()

        self.assertEquals(len(self.gglc.gramaticas), 2)

    def test_merge_de_glc_ao_carregar_do_arquivo(self):
        glc = GramaticaLivreContexto()
        glc.adiciona_producao("S", "a")
        glc.adiciona_producao("A","A b")
        self.gglc.adicionar(glc)
        self.gglc.salvar()

        self.gglc.gramaticas = []
        self.gglc.carregar()

        glc1 = GramaticaLivreContexto()
        glc1.adiciona_producao("X", "t")
        glc1.adiciona_producao("B","F q")
        self.gglc.adicionar(glc1)

        self.assertEquals(len(self.gglc.gramaticas), 2)


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

    def test_inicia_gerenciador_glc_com_gramaticas_do_arquivos(self):
        glc = GramaticaLivreContexto()
        glc.adiciona_producao("S", "a")
        glc.adiciona_producao("A","A b")
        self.gglc.adicionar(glc)
        self.gglc.salvar()

        n_gerenciador = GerenciadorGLC(self.dump)
        self.assertEquals(len(n_gerenciador.gramaticas), 1)
