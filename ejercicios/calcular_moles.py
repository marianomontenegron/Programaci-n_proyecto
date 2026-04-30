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
            self.elemento = input("Nombre del elemento o sustancia: ")
            self.masa_molar = float(input(f"Masa molar de {self.elemento} (g/mol): "))
            self.gramos = float(input("Gramos a analizar: "))
            self.moles_creidos = float(input("Predicción de moles (moles creídos): "))
            
            if self.masa_molar <= 0:
                raise ValueError("La masa molar debe ser mayor a cero.")
                
            # Cálculo directo (equivalente a la lógica de Integracion.py)
            self.moles_correctos = self.gramos / self.masa_molar
            return True
        except ValueError as e:
            print(f"Error de validación: {e}")
            return False

    def ejecutar_analisis_numerico(self):
        """
        Simula un análisis iterativo inspirado en el módulo 
        'Integracion/Integracion.py' del Proyecto Final.
        """
        print(f"\n[INICIANDO ANÁLISIS NUMÉRICO DE {self.elemento.upper()}]")
        
        # En lugar de un incremento de 1 en 1, usamos un paso infinitesimal
        # similar a los métodos de integración numérica.
        paso = 0.1
        contador_moles = 0.0
        
        while contador_moles < self.moles_correctos:
            print(f"Calculando área bajo la curva de masa... Moles: {round(contador_moles, 2)}")
            contador_moles += paso
            
            if contador_moles > self.moles_correctos:
                contador_moles = self.moles_correctos
                break
        
        print(f"Análisis completado: {round(self.moles_correctos, 4)} moles totales.")
        self.mostrar_resultado()

    def mostrar_resultado(self):
        """Lógica de comparación final"""
        error_absoluto = abs(self.moles_creidos - self.moles_correctos)
        
        print("\n" + "="*30)
        print(f"RESULTADO FINAL: {self.elemento}")
        print("="*30)
        
        if round(self.moles_creidos, 2) == round(self.moles_correctos, 2):
            print(f"PREDICCIÓN EXACTA: {self.moles_creidos} moles.")
        else:
            print(f"Predicción: {self.moles_creidos} moles.")
            print(f"Valor Real: {round(self.moles_correctos, 2)} moles.")
            print(f"Margen de error: {round(error_absoluto, 4)}")
        print("="*30)

if __name__ == "__main__":
    # Esta estructura de ejecución imita al main.py de tu proyecto
    calculadora = CalculadoraQuimicaPro()
    
    if calculadora.pedir_datos():
        calculadora.ejecutar_analisis_numerico()