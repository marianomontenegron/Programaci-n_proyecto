class SimuladorPelota:

    def __init__(self, altura_inicial, limite_altura):
        self.altura = altura_inicial
        self.limite = limite_altura
        self.coeficiente_restitucion = 0.80
        self.contador_rebotes = 0

    def ejecutar_simulacion(self):
        lineas = []
        lineas.append(f"Altura Inicial = {self.altura}m | Límite = {self.limite}m")

        if self.altura < self.limite:
            lineas.append("AVISO: La altura inicial no supera el umbral establecido.")
            return "\n".join(lineas)

        while self.altura >= self.limite:
            self.contador_rebotes += 1
            self.altura *= self.coeficiente_restitucion
            lineas.append(f"Rebote {self.contador_rebotes:02d} | Nueva Altura: {self.altura:8.3f}m")

        lineas.append(f"\nTotal de rebotes: {self.contador_rebotes}")
        lineas.append(f"Altura final: {self.altura:.4f}m")
        return "\n".join(lineas)

if __name__ == "__main__":
    try:
        h_ini = float(input("Altura de lanzamiento (m): "))
        h_lim = float(input("Altura de parada (m): "))

        if h_ini < 0 or h_lim < 0:
            print("Error: Las alturas no pueden ser negativas.")
        else:
            simulador = SimuladorPelota(h_ini, h_lim)
            print(simulador.ejecutar_simulacion())

    except ValueError:
        print("Error de entrada")