from cachorro import Cachorro
from gato import Gato
from animal import Animal

def main():
    cachorro = Cachorro()
    gato = Gato()
    animal_generico = Animal()

    cachorro.fazer_som()  # Saída: Au au!
    gato.fazer_som()      # Saída: Miau!
    animal_generico.fazer_som()  # Saída: O animal faz um som genérico.
    
main()