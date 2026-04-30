class SimuladorPelota:
    """
    Módulo de simulación física adaptado a la arquitectura de 'Proyecto_final-main'.
    Utiliza una lógica iterativa similar a los métodos de integración numérica.
    """
    def __init__(self, altura_inicial, limite_altura):
        self.altura = altura_inicial
        self.limite = limite_altura
        self.coeficiente_restitucion = 0.80  # Proporción de energía conservada
        self.contador_rebotes = 0

    def ejecutar_simulacion(self):
        """
        Calcula los rebotes de forma secuencial.
        Inspirado en la lógica de 'Integracion/Integracion.py'.
        """
        print(f"\n[INICIANDO SIMULACIÓN DE CAÍDA]")
        print(f"Configuración: Altura Inicial = {self.altura}m | Límite = {self.limite}m")
        print("-" * 50)
        
        # Validación de estado inicial
        if self.altura < self.limite:
            self.mostrar_resumen()
            return

        # Ciclo de cálculo iterativo
        while self.altura >= self.limite:
            self.contador_rebotes += 1
            self.altura *= self.coeficiente_restitucion
            
            # Salida formateada similar a los casos de prueba del proyecto
            print(f"Iteración {self.contador_rebotes:02d} | Nueva Altura: {self.altura:8.3f}m")
        
        self.mostrar_resumen()

    def mostrar_resumen(self):
        if self.contador_rebotes > 0:
            print(f"ANÁLISIS FINALIZADO")
            print(f"Total de rebotes registrados: {self.contador_rebotes}")
            print(f"Altura final alcanzada: {self.altura:.4f}m")
        else:
            print("AVISO: La altura inicial no supera el umbral establecido.")

if __name__ == "__main__":
    try:
        h_ini = float(input("Altura de lanzamiento (m): "))
        h_lim = float(input("Altura de parada (m): "))

        if h_ini < 0 or h_lim < 0:
            print("Error: Las alturas no pueden ser negativas.")
        else:
            simulador = SimuladorPelota(h_ini, h_lim)
            simulador.ejecutar_simulacion()

    except ValueError:
        print("Error de entrada: Se requiere un formato numérico (ej. 10.5).")