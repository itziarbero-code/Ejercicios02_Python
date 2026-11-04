import math

radio = int(input("Introduce el radio: "))

area = lambda radio: math.pi * radio**2

print(f"El área de la circunferencia es: {area(radio):.2f}")
