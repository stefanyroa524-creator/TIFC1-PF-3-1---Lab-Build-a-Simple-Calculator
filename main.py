
numero1 = int(input())
numero2 = int(input())
resultado = numero1 + numero2
print(resultado)

operacion = input()

if operacion == "resta":
    print(numero1 - numero2)
elif operacion == "multiplicacion":
    print(numero1 * numero2)
elif operacion == "division":
    print(numero1 / numero2)