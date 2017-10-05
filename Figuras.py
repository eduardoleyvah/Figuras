import math

class Figuras():
    def __init__(self):
        self.resultado = 0

    def obtener_resultado(self):
        return self.resultado

    def circulo(self,radio):
        self.resultado = float("{0:.2f}".format(math.pi * (radio**2),2))

    def rectangulo(self,lado_a,lado_b):
        self.resultado = lado_a * lado_b

    def cuadrado(self,lado):
        self.resultado = lado **2

    def trapecio(self,base_mayor,base_menor,altura):
        bases = base_mayor + base_menor
        self.resultado = altura * (bases/2)