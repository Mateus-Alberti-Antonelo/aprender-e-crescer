from pagamento import Pagamento

class Boleto(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento via Boleto de R${valor:.2f}")