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
