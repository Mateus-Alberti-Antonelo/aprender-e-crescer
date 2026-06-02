from cachorro import Cachorro
from animal import Animal

def main():
    meu_animal = Animal("Buddy", 3) # isso esta correto
    print(meu_animal.idade)

    meu_cachorro = Cachorro("Rex", 5, "Labrador") # isso esta correto

main()