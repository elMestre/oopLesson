class Triangle:

    def __init__(self, base, altura):
        self.name = "triángulo"
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):

        hipotenusa = (self.base**2 + self.altura**2)**0.5
        print(f"Hipotenusa { hipotenusa }")

        return self.base + self.altura + hipotenusa

    def describete(self):
        print(f"soy un { self.name }, mi base es {self.base} y mi altura {self.altura}")


class Rectangle(Triangle):

    def __init__(self, base, altura):
        super().__init__(base, altura)
        self.name = "rectángulo"

    def area(self):
        return super().area() * 2

    def perimetro(self):
        return (self.base + self.altura) * 2


class Square(Rectangle):
    def __init__(self, lado):
        super().__init__(lado, lado)

    def describete(self):
        print(f"soy un cuadrado de lado { self.base }")
