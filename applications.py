from GerenciadorGLC import GerenciadorGLC
from GramaticaLivreContexto import GramaticaLivreContexto
import tornado.ioloop
import tornado.web
import tornado.template as Template
import os
import json


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
        id -= 1
        return id

class EditHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.gerenciador_glc = GerenciadorGLC()

    def get(self, id):
        id = int(id)
        gramatica = []
        gramatica.append(self.gerenciador_glc.gramaticas[id])
        self.render("add.html",list=gramatica)

    def post(self):
        pass


def make_app():
    app = tornado.web.Application([
        (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
        (r"/", MainHandler),
        (r"/add", AddHandler),
        (r"/edit/(\d+)", EditHandler),
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