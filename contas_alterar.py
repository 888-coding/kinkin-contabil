#contas_alterar.py
import sqlite3 as s
import colorama
from colorama import Fore
from conexao import bancodados_nome
def alterar():
    dados_consultar = tela_contas_alterar()
    conta_id = consultar_conta(dados_consultar)
    if conta_id == 0:
        print("Não encontramos a conta.")
    else:
        print("Encontramos a conta !  ")
        print(conta_id)
        deseja_alterar = input("Deseja alterar ? S/N  : ").upper()
        if deseja_alterar == "S":
            print(f"Voce decidiu alterar o conta id : {conta_id}")
            conexao = s.connect(bancodados_nome)
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM contas WHERE conta_id = ?", (conta_id,))
            resultados = cursor.fetchall()
            print(f"Resultado : {resultados[0][1]}.{resultados[0][2]}: {resultados[0][3]}")
            input_descricao = input("Descrição : ").upper()
            cursor.close()
            conexao.close()
        else:
            print("Você não quer alterar")
def tela_contas_alterar():
    print(">  Alterar uma conta.")
    print("---------------------")

    print("Qual conta deseja alterar ?")
    base = input("Conta base :  ").upper()
    complementar = input("Conta complementar :  ").upper()
    dados_consultar = [base, complementar]
    return dados_consultar
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
        return conta_id
    else:
        colorama.init()
        print(Fore.RED + "Não tem resultados" + Fore.RESET)
        colorama.deinit()
        return 0
