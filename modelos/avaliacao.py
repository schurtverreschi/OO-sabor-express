class Avaliacao:
    """Representa a avaliação feita aos restaurantes."""

    def __init__(self, cliente, nota):
        """
        Inicializa a instância de Avaliação.

        Parâmetros:
        - cliente (str): Nome do cliente que fez a avaliação.
        - nota (float): Nota registrada pelo cliente.
        """
        self._cliente = cliente
        self.nota = nota  # Chama o setter automaticamente na inicialização

    @property
    def nota(self):
        """
        Nota atribuída ao objeto, limitada entre 0 e 5.

        O setter valida automaticamente o valor recebido, garantindo
        que ele permaneça no intervalo [0, 5].
        """
        return self._nota

    @nota.setter
    def nota(self, valor):
        # Aplica a trava de piso (0) e teto (5) na atribuição
        self._nota = max(0, min(valor, 5))
