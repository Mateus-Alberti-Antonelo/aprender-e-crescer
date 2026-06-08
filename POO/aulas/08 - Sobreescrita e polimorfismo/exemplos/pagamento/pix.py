from pagamento import Pagamento

class Pix(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento via Pix de R${valor:.2f}")