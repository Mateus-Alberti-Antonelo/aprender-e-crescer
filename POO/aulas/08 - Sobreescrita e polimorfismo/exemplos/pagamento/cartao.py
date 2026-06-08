from pagamento import Pagamento

class Cartao(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento via Cartão de R${valor:.2f}")