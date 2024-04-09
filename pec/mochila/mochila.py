class Articulo:
    def __init__(self, valor, peso):
        self.valor = valor
        self.peso = peso
        self.seleccionado = False

    def __str__(self):
        return f"valor = {self.valor}, " \
               f"peso = {self.peso}, " \
               f"seleccionado = {self.seleccionado}"


class Mochila:

    def __init__(self, capacidad=0):
        if capacidad < 0:
            raise ValueError("El peso maximo permitido debe ser mayor o igual a 0")
        self.articulos = []
        self.capacidad = capacidad

    def insertar_articulo(self, valor, peso):
        if valor < 0:
            raise ValueError("El valor debe ser mayor o igual a 0")
        if peso <= 0:
            raise ValueError("El peso deben ser mayores a 0")
        art = Articulo(valor, peso)
        self.articulos.append(art)

    def suma_valores(self, sumar_todos=False):
        suma = 0
        for art in self.articulos:
            if art.seleccionado or sumar_todos:
                suma += art.valor
        return suma

    def suma_pesos(self, sumar_todos=False):
        suma = 0
        for art in self.articulos:
            if art.seleccionado or sumar_todos:
                suma += art.peso
        return suma

    def valor(self):
        if self.suma_pesos() > self.capacidad:
            return -1
        else:
            return self.suma_valores()

    def articulo_de_max_valor(self, peso_disponible):
        max_valor = 0
        i = -1
        for j in range(len(self.articulos)):
            if ((not self.articulos[j].seleccionado)
                    and (self.articulos[j].valor > max_valor)
                    and (self.articulos[j].peso <= peso_disponible)):
                max_valor = self.articulos[j].valor
                i = j
        return i

    def imprimir(self, imprimir_todos=True):
        for i in range(len(self.articulos)):
            if self.articulos[i].seleccionado or imprimir_todos:
                print("articulo ", i, ": ", self.articulos[i])
        print("Maximo peso permitido: ", self.capacidad, "\n")

