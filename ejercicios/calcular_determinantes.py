class Matriz3x3:
    def __init__(self):
        self.matriz = [[0.0 for _ in range(3)] for _ in range(3)]

    def solicitar_datos(self):
        for i in range(3):
            for j in range(3):
                while True:
                    try:
                        valor = input(f"Elemento [{i+1}][{j+1}]: ")
                        self.matriz[i][j] = float(valor)
                        break
                    except ValueError:
                        print("Error: Inserte un valor numérico válido.")

    def mostrar_matriz(self):
        print("\nEstado actual de la Matriz:")
        for fila in self.matriz:
            print(f"| {fila[0]:>8.2f} {fila[1]:>8.2f} {fila[2]:>8.2f} |")

    def calcular_determinante(self, a, b, c, d, e, f, g, h, i):
        det = (a * (e * i - f * h) -
               b * (d * i - f * g) +
               c * (d * h - e * g))
        return det

if __name__ == "__main__":
    app_matriz = Matriz3x3()
    app_matriz.solicitar_datos()
    app_matriz.mostrar_matriz()
    m = app_matriz.matriz
    det_final = app_matriz.calcular_determinante(
        m[0][0], m[0][1], m[0][2],
        m[1][0], m[1][1], m[1][2],
        m[2][0], m[2][1], m[2][2]
    )
    print("\n" + "="*35)
    print(f" RESULTADO DEL DETERMINANTE: {det_final:.4f}")
    print("="*35)