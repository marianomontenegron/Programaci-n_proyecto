from PyQt5 import QtWidgets, uic
from ejercicios.calcular_determinantes import Matriz3x3

class VentanaDeterminante(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_determinantes.ui", self)
        self.show()
        self.pushButton.clicked.connect(self.botonCalcularClick)

    def botonCalcularClick(self):
        try:
            a = float(self.line_1_1.text())
            b = float(self.line_1_2.text())
            c = float(self.line_1_3.text())
            d = float(self.line_2_1.text())
            e = float(self.line_2_2.text())
            f = float(self.line_2_3.text())
            g = float(self.line_3_1.text())
            h = float(self.line_3_2.text())
            i = float(self.line_3_3.text())

        except ValueError:
            self.label_resultado.setText("Error")
            return

        determinante = Matriz3x3()
        resultado = determinante.calcular_determinante(a, b, c, d, e, f, g, h, i)
        self.matriz_1_1.setText(str(a))
        self.matriz_1_2.setText(str(b)) 
        self.matriz_1_3.setText(str(c))
        self.matriz_2_1.setText(str(d))
        self.matriz_2_2.setText(str(e))
        self.matriz_2_3.setText(str(f))
        self.matriz_3_1.setText(str(g)) 
        self.matriz_3_2.setText(str(h))
        self.matriz_3_3.setText(str(i)) 
        self.label_resultado.setText(str(resultado))