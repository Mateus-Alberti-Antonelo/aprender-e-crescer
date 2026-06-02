from gerente import Gerente
from vendedor import Vendedor

def main():
    
    gerente = Gerente("Angelo", 5000)
    vendedor = Vendedor("Maria", 3000)

    print("Gerente:")
    gerente.apresentar() # o que vai sair aqui?

    print("\nVendedor:")
    vendedor.apresentar() # o que vai sair aqui?

    # como é possivel que esteja imprimindo coisas, se minha classe Funcionario não tem o método apresentar?
    # mesma coisa para o gerente...

main()