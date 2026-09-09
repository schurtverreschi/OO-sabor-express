class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.status = False

    def __str__(self):
        return (
            f"{self.nome} | {self.categoria} | {'Ativo' if self.status else 'Inativo'}"
        )


restaurante_praca = Restaurante("Praça", "Italiana")
restaurante_pizza = Restaurante("Rhino", "Pizzaria")

print(restaurante_pizza)
print(restaurante_praca)
