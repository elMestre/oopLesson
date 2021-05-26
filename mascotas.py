class Mascota:

    def __init__(self, nombre):
        self.name = nombre
        self.palabra = None

    def presentarse(self):
        msg = "Hola"
        if hasattr(self, "especie") and self.especie:
            msg += f", soy un {self.especie}"
        else:
            msg += " no se que soy pero"

        msg += f" me llamo {self.name}"

        if hasattr(self, "palabra") and self.palabra:
            msg += f" y digo {self.palabra}."
        else:
            msg += " y no digo nada."

        print(msg)

    def hablar(self):
        print(self.palabra)


class Perro(Mascota):

    def __init__(self, nombre):
        super().__init__(nombre)
        self.especie = 'perro'
        self.palabra = 'guau'


class Gato(Mascota):

    def __init__(self, nombre):
        super().__init__(nombre)
        self.palabra = 'miau'
        self.especie = 'gato'

    def hablar(self):
        pass
