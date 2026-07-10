
numero1 = int(input())
numero2 = int(input())
operacion = input()

if operacion == "suma":
    resultado = numero1 + numero2
elif operacion == "resta":
    resultado = numero1 - numero2
elif operacion == "multiplicar":
    resultado = numero1 * numero2
elif operacion == "Dividir":
    resultado = numero1 / numero2
print(resultado)