# contas_cadastro.py 

import sqlite3 as s 
from conexao import bancodados_nome

def cadastrar():
    print("Estou dentro da funcao cadastrar")
    tela_do_cadastro()

    
def tela_do_cadastro():
    print("Tela de cadastro de Contas : ")
    base = input("Inserir a Conta BASE         : ")
    complementar = input("Inserir a conta COMPLEMENTAR : ")
    descricao = input("Inserir o nome da Conta      : ")
    print(f"A conta base é {base} , e a conta complementar é {complementar} : {descricao}")
    #CONTA BASE DEVE SER NUMERO DE ATÉ 4 CASAS.
    # ... CONTINUAR