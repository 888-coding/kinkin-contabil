#contas_alterar.py
import sqlite3 as s
from conexao import bancodados_nome
def alterar():
    dados_consultar = tela_contas_alterar()
    conta_id = consultar_conta(dados_consultar)
    if conta_id == "0":
        print("Não encontramos a conta.")
    else:
        print("Encontramos a conta !  ")
        deseja_alterar = input("Deseja alterar ? S/N  : ").upper()
        if deseja_alterar == "S":
            print("Voce decidiu alterar")
        else:
            print("Você não quer alterar")
def tela_contas_alterar():
    print(">  Alterar uma conta.")
    print("---------------------")

    print("Qual conta deseja alterar ?")
    base = input("Conta base :  ").upper()
    complementar = input("Conta complementar :  ").upper()
    dados_consultar = [base, complementar]
    return(dados_consultar)
def consultar_conta(dados_consultar):
    base = dados_consultar[0]
    complementar = dados_consultar[1]
    conexao = s.connect(bancodados_nome)
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM contas WHERE conta_base = ? and conta_complementar = ?", (base, complementar))
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    if resultados:
        conta_id = resultados[0][0]
        return (conta_id)
    else:
        print("Não tem resultados")
        return 0
