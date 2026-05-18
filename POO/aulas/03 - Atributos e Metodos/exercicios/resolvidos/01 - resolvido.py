class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)


if __name__ == "__main__":
    r1 = Retangulo(4, 2)
    r2 = Retangulo(5.5, 3)

    print("Retângulo 1")
    print(f"Largura: {r1.largura}, Altura: {r1.altura}")
    print(f"Área: {r1.calcular_area()}")
    print(f"Perímetro: {r1.calcular_perimetro()}")
    print()

    print("Retângulo 2")
    print(f"Largura: {r2.largura}, Altura: {r2.altura}")
    print(f"Área: {r2.calcular_area()}")
    print(f"Perímetro: {r2.calcular_perimetro()}")
