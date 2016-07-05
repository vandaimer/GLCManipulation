# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class EditaGlc(QWidget):

    def __init__(self, parent=None):
        super(EditaGlc, self).__init__(parent)
        self.setup()

    def setup(self):
        self.setWindowTitle("Editação GLC")

        layout = QVBoxLayout()

        groupbox = QGroupBox()
        groupbox.setMinimumSize(0,20)
        groupbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        groupbox.setObjectName("group_add_glc_%s" % layout.count())
        groupbox_layout = QHBoxLayout()
        edit = QLineEdit()
        edit.setMinimumSize(0,20)
        groupbox_layout.addWidget(edit)
        groupbox.setLayout(groupbox_layout)


        layout.addWidget(groupbox)


        self.setLayout(layout)

if __name__ == '__main__':
    import sys
    root = QApplication(sys.argv)
    app = EditaGlc()
    app.show()
    sys.exit(root.exec_())
