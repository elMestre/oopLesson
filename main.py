# !/usr/local/bin/python3

# import mascotas
from mascotas import Perro, Gato
from mascotas import Mascota

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
