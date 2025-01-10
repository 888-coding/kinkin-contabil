# contas_cadastro.py 

import sqlite3 as s 
from conexao import bancodados_nome

def cadastrar():
    print("Estou dentro da funcao cadastrar")
    dados_para_cadastro = tela_do_cadastro()
    cadastrar_conta(dados_para_cadastro)
def tela_do_cadastro():
    print("Tela de cadastro de Contas : ")
    # Checar o número Base 
    while True: 
        base = input("Inserir a Conta BASE         : ")
        if base.isdigit():
            print("O número base é dígito!")
            base = int(base)
            if base < 1 or base > 9999 :
                print("Favor escolher tamanho de 4 dígitos.")
            else:
                print("Base está correto!!")
                break
        else:
            print("O número base não é digito!")

    base = str(base)
    complementar = input("Inserir a conta COMPLEMENTAR : ").upper()
    descricao = input("Inserir o nome da Conta      : ").upper()
    dados_para_cadastro = [base, complementar, descricao]
    return dados_para_cadastro
def cadastrar_conta(dados):
    base = int(dados[0])
    complementar = dados[1]
    descricao = dados[2]
    conexao = s.connect(bancodados_nome)
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO contas (conta_base, conta_complementar, conta_descricao) VALUES (" & base & ", ")
    conexao.commit()
