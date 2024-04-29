nombre = input("Escriba su nombre completo")
print(nombre.lower())
print(nombre.upper())
print(nombre.title())

numerador = input("Ingrese el numerador ")
denominador = input("Ingrese el denominador ")
if numerador.isnumeric() and denominador.isnumeric():
    numerador = int(numerador)
    denominador = int(denominador)
    if denominador != 0:
        print(f"Resultado {numerador/denominador}")
    else:
        print("Error")
else:
    print("Error")
