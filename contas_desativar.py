#contas_desativar.py
import sqlite3 as s
from conexao import bancodados_nome
import colorama
from colorama import Fore

def desativar(conta_id):
    colorama.init()
    print(Fore.GREEN + "Desativar a conta" + Fore.RESET)
    colorama.deinit()
    conexao = s.connect(bancodados_nome)
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM contas WHERE conta_id = ?", (conta_id))
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()

    # Mostrar na tela
    colorama.init()
    print( Fore.GREEN + "Você tem certeza que quer desativar esta conta ? " + Fore.RESET)
    colorama.deinit()
    print(f"Conta: {resultados[0][1]} . {resultados[0][2]} = {resultados[0][3]}")
    deseja_desativar = input("S / N ? ").upper()

    # Desativar
    if deseja_desativar == "S":
        conexao = s.connect(bancodados_nome)
        cursor = conexao.cursor()
        cursor.execute("UPDATE contas SET desativar = 1 WHERE conta_id = ?", (resultados[0][0]))
        conexao.commit()
        colorama.init()
        print(Fore.GREEN + "Conta desativada com sucesso" + Fore.RESET)
        colorama.deinit()
    else:
        colorama.init()
        print(Fore.GREEN + "Não foi alterado" + Fore.RESET)
        colorama.deinit()
