class Restaurante:

    restaurantes = []  # noqa: RUF012

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._status = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self._nome} | {self._categoria} | {self._status}"

    @classmethod
    def listar_restaurantes(cls):
        print(f"\n{'Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status")
        for restaurante in cls.restaurantes:
            print(
                f"{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.status}"
            )

    def alternar_status(self):
        self._status = not self._status

    @property
    def status(self):
        return "✔️" if self._status else "❌"
