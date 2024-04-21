class Operations:
    def __init__(self, lista, numero, palabra):
        self.lista = lista
        self.numero = numero
        self.palabra = palabra

    def suma(self):
        if type(self.lista) == list:
            print(f"Sum of list: {sum(self.lista)}")
        else:
            print("Argument is not a list")

    def cuadrado(self):
        if type(self.numero) == int:
            print(f"Square of int: {self.numero ** 2}")
        else:
            print("Argument is not an integer")

    def texto(self):
        if type(self.palabra) == str:
            print(f"String: {self.palabra}")
        else:
            print("Argument is not a string")


Math = Operations([1, 2, 3, 4], 5, "El PEPE")
Math.suma()
Math.cuadrado()
Math.texto()
