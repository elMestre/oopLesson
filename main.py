# !/usr/local/bin/python3

# import mascotas
from mascotas import Mascota, Perro, Gato
from figures import Triangle, Rectangle, Square


def ejemploMascota():
    mascotas = [
        Mascota('Chtulu'),
        Gato('Isidoro'),
        Perro('Lassie'),
        Perro('Tobby'),
        Perro('Rango'),
        Gato('Michi')
    ]

    for mascota in mascotas:
        print(type(mascota))
        mascota.presentarse()
        mascota.hablar()


def ejemploFiguras():

    figuras = [
        Rectangle(2, 3),
        Square(2),
        Triangle(2, 3)
    ]

    for forma in figuras:
        print(type(forma))
        print(f"Area: { forma.area() } m2")
        print(f"Perimetro: { forma.perimetro() } m")
        forma.describete()
        print("\n")


ejemploMascota()
ejemploFiguras()
