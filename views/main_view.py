from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

from datetime import *

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('views/vista.ui', self)

        self.frame_modulos.hide()

        self.suma_di = []
        self.multi_di = []
        self.aux: int = 0
        self.idFactura = 0
        self.today = date.today()
        self.acumulador = 1
        self.total = 0
        # Botones y funciones
        self.btn_inicio.clicked.connect(self.inicio_sesion)
        self.btn_modulo_suma.clicked.connect(self.show_page_suma)
        self.btn_modulo_multi.clicked.connect(self.show_page_multi)


        # botones doctor
        self.btn_ingresar_suma.clicked.connect(self.cargar_suma)
        self.btn_resultado_suma.clicked.connect(self.efectuar_suma)
        self.btn_ingresar_multi.clicked.connect(self.cargar_multi)
        self.btn_resultado_multi.clicked.connect(self.efectuar_multi)

    # Funcionalidad de botones

    def inicio_sesion(self):
        self.frame_modulos.show()

    def show_page_suma(self):
        self.stackedWidget.setCurrentWidget(self.page_suma)

    def show_page_multi(self):
        self.stackedWidget.setCurrentWidget(self.page_multi)

    def cargar_suma(self):
        try:
            numero = self.ln_suma.text()
            self.suma_di.append(numero)
            self.ln_suma.clear()
        except Exception as e:
            print(e)

    def efectuar_suma(self):
        try:
            resultado = 0
            for i in self.suma_di:
                resultado = resultado + int(i)
            self.resultado_lab_suma.setStyleSheet('font: 48pt "MS Shell Dlg 2";')
            self.resultado_lab_suma.setAlignment(Qt.AlignCenter)
            self.resultado_lab_suma.setText(str(resultado))
            self.suma_di.clear()
        except Exception as e:
            print(e)

    def cargar_multi(self):
        try:
            numero = self.ln_multi.text()
            self.multi_di.append(numero)
            self.ln_multi.clear()
        except Exception as e:
            print(e)

    def efectuar_multi(self):
        try:
            resultado = 1
            for i in self.multi_di:
                resultado = resultado * int(i)
            self.resultado_lab_multi.setStyleSheet('font: 48pt "MS Shell Dlg 2";')
            self.resultado_lab_multi.setAlignment(Qt.AlignCenter)
            self.resultado_lab_multi.setText(str(resultado))
            self.multi_di.clear()
        except Exception as e:
            print(e)
