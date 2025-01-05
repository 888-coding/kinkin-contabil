# contas_cadastro.py 

import sqlite3 as s 
from conexao import bancodados_nome

def cadastrar():
    print("Estou dentro da funcao cadastrar")
    tela_do_cadastro()

    
def tela_do_cadastro():
    print("Tela de cadastro de Contas : ")
    while True: 
        base = input("Inserir a Conta BASE         : ")
        if base.isdigit():
            print("O número base é digito!")
            base = int(base)
            if base < 1 or base > 9999 :
                print("Favor escolher tamanho de 4 digitos.")
            else:
                print("Base está correto!!")
                break
        else:
            print("O número base não é digito!")
    
    complementar = input("Inserir a conta COMPLEMENTAR : ")
    descricao = input("Inserir o nome da Conta      : ")
    print(f"A conta base é {base} , e a conta complementar é {complementar} : {descricao}")
    #CONTA BASE DEVE SER NUMERO DE ATÉ 4 CASAS.
    # ... Não pode ser mais que 9999. 

    
    
