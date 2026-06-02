from cachorro import Cachorro
from gato import Gato

def main():
    cachorro = Cachorro()
    gato = Gato()

    print(cachorro)
    cachorro.comer()
    
    print(gato)    
    gato.comer()

main()