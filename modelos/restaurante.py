from modelos.avaliacao import Avaliacao


class Restaurante:
    """Representa um restaurante e suas características."""

    restaurantes = []  # noqa: RUF012

    def __init__(self, nome, categoria):
        """
        Inicializa a instancio de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._status = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f"{self._nome} | {self._categoria} | {self._status}"

    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada com todos os restaurantes."""
        print(
            f"\n{'Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | Status"
        )
        for restaurante in cls.restaurantes:
            print(
                f"{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.status}"
            )

    def alternar_status(self):
        """Altera o estado de atividade do restaurante."""
        self._status = not self._status

    @property
    def status(self):
        """Exibe um simbolo selecionado indicando o estado de atividade do restaurante."""
        return "✔️" if self._status else "❌"

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): Nome do cliente que fez a avaliação.
        - nota (float): Nota atribuida ao restaurante (entre 0 e 5).
        """
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """Calcula e retorna o valor da media das avaliações recebidas pelo restaurante."""
        if not self._avaliacao:
            return "Novo"
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
