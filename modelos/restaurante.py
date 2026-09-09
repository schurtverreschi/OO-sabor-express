class Restaurante:

    restaurantes = []  # noqa: RUF012

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._status = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self.nome} | {self.categoria} | {self._status}"

    def listar_restaurantes():
        print(f"\n{'Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status")
        for restaurante in Restaurante.restaurantes:
            print(
                f"{restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {restaurante.status}"
            )

    @property
    def status(self):
        return "✔️" if self._status else "❌"


restaurante_praca = Restaurante("Praça", "Italiana")
restaurante_pizza = Restaurante("Rhino", "Pizzaria")

Restaurante.listar_restaurantes()
