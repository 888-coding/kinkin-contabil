#contas_alterar.py
import sqlite3 as s
from conexao import bancodados_nome

def tela_contas_alterar():
    print(">  Alterar uma conta.")
    print("---------------------")

    print("Qual conta deseja alterar ?")
    base = input("Conta base :  ")
    complementar = input("Conta complementar :  ")
    dados_consultar = [base, complementar]
    print(dados_consultar)