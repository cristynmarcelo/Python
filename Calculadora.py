import os
os.system('cls')
num1 = int(input(f"Número 1: "))
op = input("Operação: ")
num2 = input("Número 2: ")
equacao = f"{num1}{op}{num2}"
resultado = eval(equacao)
print(resultado)