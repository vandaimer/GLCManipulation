from GerenciadorGLC import GerenciadorGLC
from GramaticaLivreContexto import GramaticaLivreContexto
import tornado.ioloop
import tornado.web
import tornado.template as Template
import os


class MainHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.gerenciador_glc = GerenciadorGLC()

    def get(self):
        gramaticas = self.gerenciador_glc.gramaticas
        self.render("index.html", list=gramaticas)


class AddHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.gerenciador_glc = GerenciadorGLC()

    def get(self):
        id = self.createGLC()
        if id != False:
            return self.redirect('edit/%s' % id)

    def createGLC(self):
        nGLC = GramaticaLivreContexto()
        add = self.gerenciador_glc.adicionar(nGLC)
        if not add:
            return False

        save = self.gerenciador_glc.salvar()
        if  not save:
            return False

        id = len(self.gerenciador_glc.gramaticas)
        if id > 0:
            id -= 1
        return str(id)

class EditHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.gerenciador_glc = GerenciadorGLC()

    def get(self, id):
        id = int(id)
        gramatica = self.gerenciador_glc.gramaticas[id]
        identificador = gramatica.identificador
        self.render("edit.html", producoes=gramatica.producoes, identificador=identificador,
                    id=id)

    def post(self, id):
        id = int(id)
        producoes = self.get_arguments('producao[]')
        identificador = self.get_argument('identificador')
        nGramatica = GramaticaLivreContexto(identificador)
        for producao in producoes:
            producao = producao.split(' -> ')
            nGramatica.adiciona_producao(producao[0], producao[1])

        self.gerenciador_glc.gramaticas[id] = nGramatica
        save = self.gerenciador_glc.salvar()
        if not save:
            return False
        return self.redirect('/')


class DeleteHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.gerenciador_glc = GerenciadorGLC()

    def get(self, id):
        id = int(id)
        return self.deleteGLC(id)

    def deleteGLC(self, id):
        del self.gerenciador_glc.gramaticas[id]
        self.gerenciador_glc.salvar()
        return self.redirect('/')


class DetailsHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.gerenciador_glc = GerenciadorGLC()

    def get(self, id):
        id = int(id)
        gramatica = self.gerenciador_glc.obtem_by_index(id)
        producoes = gramatica.producoes
        recursao_esquerda_direta = gramatica.recursao_esquerda_direta()
        recursao_esquerda_indireta = gramatica.recursao_esquerda_indireta()
        if gramatica != False:
            first = gramatica.get_all_first()
            follow = gramatica.get_all_follow()
            self.render("details.html", producoes=producoes,
                        recursao_esquerda_direta=recursao_esquerda_direta,
                        recursao_esquerda_indireta=recursao_esquerda_indireta,
                        first=first, follow=follow)


def make_app():
    app = tornado.web.Application([
        (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
        (r"/", MainHandler),
        (r"/add", AddHandler),
        (r"/edit/(\d+)", EditHandler),
        (r"/delete/(\d+)", DeleteHandler),
        (r"/details/(\d+)", DetailsHandler),
    ], autoreload=True)

    app.settings = {
        "template_path":"view",
        "static_path":"static"
    }

    return app

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)

    #SOMENTE EM DEV
    for dir, _, files in os.walk('view'):
        [tornado.autoreload.watch(dir + '/' + f) for f in files if not f.startswith('.')]

    template = Template.Loader("view")
    tornado.ioloop.IOLoop.current().start()
