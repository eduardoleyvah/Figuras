import unittest

from Figuras import Figuras

class FigurasTest(unittest.TestCase):

	def setUp(self):
		self.area = Figuras()

	def test_Circulo(self):
		self.area.circulo(4)
		self.assertEquals(self.area.obtener_resultado(),50.27)

	def test_Rectangulo(self):
		self.area.rectangulo(6,4)
		self.assertEquals(self.area.obtener_resultado(),24)

	def test_Cuadrado(self):
		self.area.cuadrado(4)
		self.assertEquals(self.area.obtener_resultado(),16)

	def test_Trapezio(self):
		self.area.trapecio(15,5,7)
		self.assertEquals(self.area.obtener_resultado(),70)

if __name__ == '__main__': #pragma: no cover
	unittest.main()