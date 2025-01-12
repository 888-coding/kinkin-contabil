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
    print("CODIGO BASE     CODIGO COMPLEMENTAR       DESCRICAO     ")
    for resultado in resultados:
        print(f"{resultado[1]}   {resultado[2]}            {resultado[3]}")

