# contas_buscar_todos.py
import sqlite3 as s
from conexao import bancodados_nome

def mostratodos():
    conexao = s.connect(bancodados_nome)
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM contas")
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    print("Cadastro de contas:")
    print("CODIGO BASE      CODIGO COMPLEMENTAR  DESCRICAO           ")
    for resultado in resultados:
        coluna = 1
        coluna_maxima = 20
        for caracter in resultado[1]:
            print(f"{caracter}", end="")
            coluna = coluna + 1
        caracter = ""
        while coluna != coluna_maxima:
            print(" ", end="")
            coluna = coluna + 1
        coluna = 1
        for caracter in resultado[2]:
            print(f"{caracter}", end="")
            coluna = coluna + 1
        while coluna != coluna_maxima:
            print(" ", end="")
            coluna = coluna + 1
        coluna = 1
        for carater in resultado[3]:
            print(f"{carater}", end="")
            coluna = coluna + 1
        while coluna != coluna_maxima:
            print(" ", end="")
            coluna = coluna + 1
        print("")

