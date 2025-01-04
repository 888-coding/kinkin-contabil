# contas_buscar_todos.py
import sqlite3 as s
from conexao import bancodados_nome

def mostratodos():
    conexao = s.connect(bancodados_nome)
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM contas")
    resultados = cursor.fetchall()
    conexao.close()
    print(resultados)
