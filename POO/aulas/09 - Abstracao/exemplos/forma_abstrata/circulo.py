from forma import Forma
import math

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
         return math.pi * self.raio ** 2