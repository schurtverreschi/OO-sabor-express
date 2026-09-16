class Avaliacao:

    def __init__(self, cliente, nota):
        self._cliente = cliente
        self.nota = nota  # Chama o setter automaticamente na inicialização

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor):
        # Aplica a trava de piso (0) e teto (5) na atribuição
        self._nota = max(0, min(valor, 5))
