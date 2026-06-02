import gato
from cachorro import Cachorro

def main():
    # Criando um objeto da classe Cachorro
    meu_cachorro = Cachorro("Rex", 5)
    print(meu_cachorro)

    # Criando um objeto da classe Gato
    meu_gato = gato.Gato("Faisca", 3)
    print(meu_gato)

main()