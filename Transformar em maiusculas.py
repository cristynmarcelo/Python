import pandas as pd
import os
from tkinter import TRUE
os.system('cls')
teste = 0



while True:
    NOME = input("nome: ")
    NOME = NOME.upper()
    df=pd.DataFrame([NOME])
    df.to_clipboard(index=False,header=False)
    print("-="*30 + "\n")
    #print()
    print(NOME + "\n")
    print("-="*30)
    print(" "*500)
    input("aperte Enter pra continuar")
    os.system('cls')


