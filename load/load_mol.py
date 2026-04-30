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
            elemento = self.lineEdit_elemento.text()
            masa_molar = float(self.lineEdit_masa_molar.text())
            gramos = float(self.lineEdit_g.text())
            moles_creidos = float(self.lineEdit_prediccion_moles.text())
        except ValueError:
            self.label_resultado.setText("Error: ingresa valores numéricos válidos.")
            return

        calculadora = CalculadoraQuimica()
        calculadora.elemento = elemento
        calculadora.masa_molar = masa_molar
        calculadora.gramos = gramos
        calculadora.moles_creidos = moles_creidos

        if not calculadora.pedir_datos():
            self.label_resultado.setText("Error: la masa molar debe ser mayor a cero.")
            return

        analisis = calculadora.ejecutar_analisis_numerico()
        resultado = calculadora.obtener_resultado()
        self.label_resultado.setText(f"{analisis}\n\n{resultado}")