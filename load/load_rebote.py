from PyQt5 import QtWidgets, uic
from ejercicios.calcular_rebotes import SimuladorPelota

class VentanaRebotes(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_rebotes.ui", self)
        self.show()
        self.BotonCalcular.clicked.connect(self.botonCalcularClick)

    def botonCalcularClick(self):
        try:
            h_ini = float(self.line_h_inicial.text())
            h_lim = float(self.line_h_min.text())
        except ValueError:
            self.label_resultado.setText("Error")
            return

        if h_lim < 0:
            self.label_resultado.setText("La altura de parada no puede ser negativa")
            return

        simulador = SimuladorPelota(h_ini, h_lim)
        resultado = simulador.ejecutar_simulacion()
        self.label_resultado.setText(str(resultado))