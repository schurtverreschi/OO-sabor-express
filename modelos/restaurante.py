class Restaurante:

    restaurantes = []  # noqa: RUF012

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.status = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return (
            f"{self.nome} | {self.categoria} | {'Ativo' if self.status else 'Inativo'}"
        )

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(
                f"{restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {restaurante.status}"
            )


restaurante_praca = Restaurante("Praça", "Italiana")
restaurante_pizza = Restaurante("Rhino", "Pizzaria")

Restaurante.listar_restaurantes()
