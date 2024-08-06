from programa import imprimir_datos_personales
from io import StringIO
import sys

def test_imprimir_datos_personales(capsys):
    nombre = "Anthony Robayo"
    edad = 26
    estatura = 1.68
    imprimir_datos_personales(nombre, edad, estatura)
    captured = capsys.readouterr()
    assert captured.out == "Nombre: Anthony Robayo\nEdad: 26\nEstatura: 1.68\n"
