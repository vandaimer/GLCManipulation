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
        self.write(template.load("index.html").generate(gramaticas=gramaticas))

class AddHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.gerenciador_glc = GerenciadorGLC()

    def get(self):
        self.render("add.html")

    def post(self):
        try:
            data = tornado.escape.to_basestring(self.request.body)
            data = json.loads(data)

            nGLC = GramaticaLivreContexto()
            for NT,producao in data.items():
                nGLC.adiciona_producao(NT, producao)

            add = self.gerenciador_glc.adicionar(nGLC)
            if not add:
                return self.set_status(400, "Não adicionada a GLC")

            save = self.gerenciador_glc.salvar()
            if  not save:
                return self.set_status(400, "Não salvo a GLC")
        except Exception as e:
            print(e)
            self.set_status(400, "Bad Content")


def make_app():
    app = tornado.web.Application([
        (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
        (r"/", MainHandler),
        (r"/add", AddHandler),
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
