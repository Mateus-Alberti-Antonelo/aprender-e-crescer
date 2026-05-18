class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def exibir_ficha(self):
        disponibilidade = "Disponível" if self.esta_disponivel() else "Esgotado"
        print(f"Produto: {self.nome} | Preço: R$ {self.preco:.2f} | Estoque: {self.estoque} | {disponibilidade}")

    def esta_disponivel(self):
        return self.estoque > 0


if __name__ == "__main__":
    p1 = Produto("Teclado Mecânico", 349.90, 15)
    p2 = Produto("Mouse Gamer", 189.00, 0)

    p1.exibir_ficha()
    p2.exibir_ficha()
    print(p2.esta_disponivel())
