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
    print("CODIGO BASE         CODIGO COMPLEMENTAR DESCRICAO           ")
    # 列印資料庫的內容
    for resultado in resultados:
        coluna = 1
        coluna_maxima = 20
        # NumeroCampoTabela 是指資料庫裡的列表中的資料, 譬如: 1 是 主號碼
        NumeroCampoTabela = 1
        while NumeroCampoTabela <= 3:
            for cada_caracter in resultado[NumeroCampoTabela]:
                print(f"{cada_caracter}", end="")
                coluna = coluna + 1
            cada_caracter = ""
            # 如果每個coluna 沒有到最高數, 加空白鍵
            while coluna != coluna_maxima:
                print(" ", end="")
                coluna = coluna + 1
            coluna = 1
            NumeroCampoTabela = NumeroCampoTabela + 1
        print("end")