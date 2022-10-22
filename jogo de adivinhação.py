import os
import random
os.system('cls')

erros = 0
nSorteado = random.randrange(0,20)
print("Tente acertar o número sorteado, digite um número entre 0 e 20")
print("-="*31)
print()
jogador = int(input("Digite um número: "))

while(nSorteado!=jogador):
    os.system('cls')
    if(nSorteado>jogador):
        print("Tente acertar o número sorteado, digite um número entre 0 e 20")
        print("-="*31 + "\n")
        print("ERROU! o numero é maior")
    elif(nSorteado<jogador):
        print("Tente acertar o número sorteado, digite um número entre 0 e 20")
        print("-="*31 + "\n")
        print("ERROU! o numero é menor")
    erros+=1
    jogador=int(input("Digite um numero: "))
    print()
    print("-="*31)
print(f"Acertou miseravi!, vc consegui em " + {erros+1} + " tentativas")
