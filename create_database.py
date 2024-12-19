# Criação de Banco de dados 
# - Fazer condição para não ter duplicidade
# - Nome do banco de dados : contabilidade.db 

import os
import sqlite3 as s

nome_arquivo = "contabilidade.db"

if os.path.exists(nome_arquivo):
    print("O arquivo já existe")
else:
    # Criação de banco de dados
    conexao = s.connect("contabilidade.db")
    conexao.close()
    print("Criação do arquivo com sucesso")

