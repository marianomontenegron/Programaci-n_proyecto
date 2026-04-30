from PyQt5 import QtWidgets, uic, QtCore        
from load.load_det import VentanaDeterminante
from load.load_mol import VentanaCalcularMoles
from load.load_rebote import VentanaRebotes

class MenuPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_menu_principal.ui", self)
        self.showMaximized()

        self.actionCalculadora_determinantes.triggered.connect(self.ingresardeterminantes)
        self.actionCalculadora_moles.triggered.connect(self.ingresarmoles)
        self.actionCalculadora_rebotes.triggered.connect(self.ingresarrebotes)
    
        self.actionSalir.triggered.connect(self.salir)

    def ingresarmoles(self):
        moles = VentanaCalcularMoles()
        moles.exec() 

    def ingresardeterminantes(self):
        determinantes = VentanaDeterminante()
        determinantes.exec()

    def ingresarrebotes(self):
        rebotes = VentanaRebotes()
        rebotes.exec()

    def salir(self):
        self.close()