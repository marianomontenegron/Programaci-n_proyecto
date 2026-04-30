from PyQt5 import QtWidgets, uic
from ejercicios.calcular_moles import CalculadoraQuimica

class VentanaCalcularMoles(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_Calcular_moles.ui", self)
        self.show()
        self.Boton_calc.clicked.connect(self.botonCalcularClick)

    def botonCalcularClick(self):
        try:
            elemento = float(self.lineEdit_elemento.text())
            masa_molar = float(self.lineEdit_masa_molar.text())
            gramso = float(self.lineEdit_gramos.text())
            moles_creidos = float(self.lineEdit_prediccion_moles.text())
        except ValueError:
            self.label_resultado.setText("Error")
            return

        calculadora = CalculadoraQuimica()
        calculadora.elemento = elemento
        calculadora.masa_molar = masa_molar
        calculadora.gramos = gramso
        calculadora.moles_creidos = moles_creidos

        if not calculadora.pedir_datos():
            return

        self.label_resultado.setText(f"Moles correctos: {calculadora.moles_correctos}")