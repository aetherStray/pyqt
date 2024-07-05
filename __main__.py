import sys
from PyQt5.QtWidgets import QApplication
import gui_pyqt5


class App(QApplication):

    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.gui = gui_pyqt5.AplicacionGui()


if __name__ == '__main__':

    app = App(sys.argv)
    sys.exit(app.exec_())
