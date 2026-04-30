from PyQt5 import QtWidgets, uic, QtCore        
from load.load_det import Matriz3x3
from load.load_mol import CalculadoraQuimica
from load.load_rebote import SimuladorPelota 

class MenuPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_menu_principal.ui", self)
        self.showMaximized()

        self.actionCalculadora_determinantes.triggered.connect(self.ingresarmoles)
        self.actionCalculadora_moles.triggered.connect(self.ingresardeterminantes)
        self.actionCalculadora_rebotes.triggered.connect(self.ingresarrebotes)
        
        self.actionSalir.triggered.connect(self.salir)

    def ingresarmoles(self):
        moles = CalculadoraQuimica()
        moles.exec()

    def ingresardeterminantes(self):
        determinantes = Matriz3x3()
        determinantes.exec()

    def ingresarrebotes(self):
        rebotes = SimuladorPelota() 

    def salir(self):
        self.close()
