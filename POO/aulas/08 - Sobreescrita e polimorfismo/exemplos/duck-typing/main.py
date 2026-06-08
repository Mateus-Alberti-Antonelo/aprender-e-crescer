from animal import Animal
from carro import Carro

def main():
    
    animal = Animal()
    carro = Carro()

    meus_objetos = [animal, carro]

    for obj in meus_objetos:
        obj.emitir_som() #python nao quer saber de que tipo é o objeto, ele só quer saber se ele tem o método emitir_som
    
main()