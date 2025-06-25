import random

elementos = "+-/*!&$#?=@<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

largo = int(input("introduse la longitud de tu contraseña segura: "))

contrasena = ""

for i in range(largo):
    contrasena += random.choice(elementos)

print(f"Tu nueva contraseña segura es: {contrasena} ")
