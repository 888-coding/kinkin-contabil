#contas_alterar.py
import sqlite3 as s
from conexao import bancodados_nome
def alterar():
    tela_contas_alterar()
def tela_contas_alterar():
    print(">  Alterar uma conta.")
    print("---------------------")

    print("Qual conta deseja alterar ?")
    base = input("Conta base :  ")
    complementar = input("Conta complementar :  ")
    dados_consultar = [base, complementar]

    conexao = s.connect(bancodados_nome)
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM contas WHERE conta_base = ? and conta_complementar = ?", (base, complementar))
    resultados = cursor.fetchall()
    if resultados:
        for resultado in resultados:
            print(resultado[0])
            print(resultado[1])
            print(resultado[2])
    else:
        print("Não tem resultados")
    cursor.close()
    conexao.close()
