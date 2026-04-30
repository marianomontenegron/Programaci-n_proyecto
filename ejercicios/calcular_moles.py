import math

class CalculadoraQuimica:

    def __init__(self):
        self.elemento = ""
        self.masa_molar = 0.0
        self.gramos = 0.0
        self.moles_creidos = 0.0
        self.moles_correctos = 0.0
        
    def pedir_datos(self):
        try:
            if self.masa_molar <= 0:
                raise ValueError("La masa molar debe ser mayor a cero.")
            self.moles_correctos = self.gramos / self.masa_molar
            return True
        except ValueError:
            return False

    def ejecutar_analisis_numerico(self):
        paso = 1.0
        contador_moles = 0.0
        lineas = [f"Analizando {self.gramos}g de {self.elemento}..."]
    
        while contador_moles < self.moles_correctos:
            contador_moles += paso
            if contador_moles > self.moles_correctos:
                contador_moles = self.moles_correctos
            lineas.append(f"Verificando... : {round(contador_moles, 2)} moles")
    
        return "\n".join(lineas)

    def obtener_resultado(self):
        error_absoluto = abs(self.moles_creidos - self.moles_correctos)
        
        if round(self.moles_creidos, 2) == round(self.moles_correctos, 2):
            return f"PREDICCIÓN EXACTA: {self.moles_creidos} moles."
        else:
            return (
                f"Elemento: {self.elemento}\n"
                f"Predicción: {self.moles_creidos} moles\n"
                f"Valor real: {round(self.moles_correctos, 2)} moles\n"
                f"Margen de error: {round(error_absoluto, 4)}"
            )

if __name__ == "__main__":
    calculadora = CalculadoraQuimica()
    if calculadora.pedir_datos():
        calculadora.ejecutar_analisis_numerico()