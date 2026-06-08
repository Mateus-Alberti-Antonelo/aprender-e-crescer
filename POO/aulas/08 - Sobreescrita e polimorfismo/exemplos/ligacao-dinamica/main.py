from cachorro import Cachorro
from gato import Gato
from animal import Animal

def main():
    
    meu_animal = Cachorro()
    meu_animal.fazer_som()  # Saída: Au au!

    meu_animal = Gato()
    meu_animal.fazer_som()  # Saída: Miau!

    meu_animal = Animal()
    meu_animal.fazer_som()  # Saída: O animal faz um som

main()