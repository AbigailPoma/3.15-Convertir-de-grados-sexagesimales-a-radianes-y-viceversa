import math

def grados_a_radianes():
    grados = float(input("Ingresa el ángulo en grados: "))
    radianes = math.radians(grados)
    print(f"{grados} grados es igual a {radianes} radianes")

def radianes_a_grados():
    radianes = float(input("Ingresa el ángulo en radianes: "))
    grados = math.degrees(radianes)
    print(f"{radianes} radianes es igual a {grados} grados")

# Llamada a las funciones
grados_a_radianes()
radianes_a_grados()
