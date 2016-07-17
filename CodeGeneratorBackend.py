#
# a Python code generator backend
#
# fredrik lundh, march 1998
#
# fredrik@pythonware.com
# http://www.pythonware.com
#

class CodeGeneratorBackend:

    def begin(self, tab="\t"):
        self.code = []
        self.tab = tab
        self.level = 0

    def end(self):
        # return string.join(self.code, "")
        return "".join(self.code)

    def write(self, string):
        self.code.append(self.tab * self.level + string +"\n")

    def indent(self):
        self.level = self.level + 1

    def dedent(self):
        if self.level == 0:
            raise SyntaxError("internal error in code generator")
        self.level = self.level - 1