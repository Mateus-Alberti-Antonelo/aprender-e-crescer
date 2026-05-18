class Usuario:
    def __init__(self, nome, email, cargo="Visitante", ativo=True):
        self.nome = nome
        self.email = email
        self.cargo = cargo
        self.ativo = ativo

    def apresentar(self):
        status = "Ativo" if self.ativo else "Inativo"
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Cargo: {self.cargo}")
        print(f"Status: {status}")
        print()


if __name__ == "__main__":
    u1 = Usuario("Ana", "ana@example.com")
    u2 = Usuario("Bruno", "bruno@example.com", cargo="Editor")
    u3 = Usuario("Carla", "carla@example.com", cargo="Administrador", ativo=False)

    u1.apresentar()
    u2.apresentar()
    u3.apresentar()
