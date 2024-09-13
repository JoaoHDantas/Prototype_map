import copy

class PrototypeCelular:
    # Método de clonagem utilizando a biblioteca copy
    def clone(self):
        return copy.deepcopy(self)

# Celular é a classe concreta que implementa o PrototypeCelular
class Celular(PrototypeCelular):
    # Construtor do celular
    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    # Método para exibir as informações do celular
    def __str__(self):
        return f'Celular (Modelo={self.modelo}, cor={self.cor}, preço={self.preco})'

# Uando o padrão Prototype
if __name__ == "__main__":
    celular1 = Celular("Iphone13", "Branco", 4000)
    print(f"Celular1 original: {celular1}")

    # Clonando o objeto celular1
    celular2 = celular1.clone()
    print(f"Clone do celular1 (Celular2): {celular2}")

    # Alterando informações do clone de celular1
    celular2.cor = "verde"
    celular2.preco = "3500"
    print(f"Celular2 depois de mudar informaçoes: {celular2}")
    print(f"Celular1 continundo com as informaçoes inicias: {celular1}")
