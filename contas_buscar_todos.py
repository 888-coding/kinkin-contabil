# contas_buscar_todos.py
import sqlite3 as s
from conexao import bancodados_nome
import colorama
from  colorama import Fore

def mostratodos():
    conexao = s.connect(bancodados_nome)
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM contas")
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    colorama.init()
    print(Fore.GREEN + "Lista de todas as contas:" + Fore.RESET)
    colorama.deinit()
    print("CODIGO BASE      CODIGO COMPLEMENTAR  DESCRICAO           ")
    for resultado in resultados:
        coluna = 1
        coluna_maxima = 20
        i = 1
        while i < 4:
            for caracter in resultado[i]:
                print(f"{caracter}", end="")
                coluna = coluna + 1
            caracter = ""
            while coluna != coluna_maxima:
                print(" ", end="")
                coluna = coluna + 1
            coluna = 1
            i = i + 1
        print("")

