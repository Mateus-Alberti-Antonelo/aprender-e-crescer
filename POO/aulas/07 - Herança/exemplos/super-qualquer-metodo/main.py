from cargos import Gerente, Coordenador, Motorista, Secretario
def main():
    
    coord = Coordenador("Maria", 3000)
    coord.apresentar()

    ger = Gerente("João", 5000)
    ger.apresentar()

    motorista = Motorista("Carlos", 2000)
    motorista.apresentar()

    secretario = Secretario("Ana", 2500)
    secretario.apresentar()

main()