from modelos.restaurante import Restaurante

restaurante_pizza = Restaurante("rhino", "Pizzaria")
restaurante_hamburguer = Restaurante("olk", "Hamburgueria")
restaurante_mineira = Restaurante("Panela", "Mineira")

restaurante_mineira.alternar_status()


def main():
    Restaurante.listar_restaurantes()


if __name__ == "__main__":
    main()
