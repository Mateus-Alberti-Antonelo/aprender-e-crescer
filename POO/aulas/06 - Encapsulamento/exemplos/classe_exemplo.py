class Exemplo:
    def __init__(self):
        self.publico = "Todo mundo vê"           # 🌍 Público
        self._protegido = "Uso interno"          # 🔒 Protegido
        self.__privado = "Bem escondido"         # 🔐 Privado
    
    def metodo_publico(self):                    # 🌍 Público
        pass
    
    def _metodo_protegido(self):                 # 🔒 Protegido
        pass
    
    def __metodo_privado(self):                  # 🔐 Privado
        pass