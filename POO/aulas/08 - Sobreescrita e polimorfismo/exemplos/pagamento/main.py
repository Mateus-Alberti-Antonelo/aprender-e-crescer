from cartao import Cartao
from boleto import Boleto
from pix import Pix

def finalizar_venda(metodo_pagamento, valor):
    metodo_pagamento.processar_pagamento(valor) # essa funcao nao precisa saber como a forma de pagamento processa as coisas, só manda processar

    # aqui vem o resto de tudo, imprimir a nota, gerar pedido, etc

def main():
    #imagine que fiz toda a minha compra, e agora ta na hora de pagar
    valor_total = 150.75

    # vou chamar uma funcao chamada "finalizar_venda" e passar o metodo de pagamento, e o valor
    finalizar_venda(Cartao(), valor_total)
    finalizar_venda(Boleto(), valor_total)
    finalizar_venda(Pix(), valor_total)
main()