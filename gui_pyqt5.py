from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QGroupBox, QGridLayout, QLabel, QLineEdit, QVBoxLayout

class AplicacionGui(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "Webos"
        self.left = 80
        self.top = 80
        self.width = 720
        self.height = 480
        self.IniciarGui()

    def IniciarGui(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.distribucion_vertical = QVBoxLayout()
        
        self.caja_materias = QGroupBox("Materias")
        self.caja_botones = QGroupBox()

        distribucion_caja_materias = QGridLayout()
        distribucion_caja_botones = QHBoxLayout()

        self.caja_materias.setLayout(distribucion_caja_materias)
        self.caja_botones.setLayout(distribucion_caja_botones)

        self.distribucion_vertical.addWidget(self.caja_materias)
        self.distribucion_vertical.addWidget(self.caja_botones)

        self.setLayout(self.distribucion_vertical)
        
        self.show()


