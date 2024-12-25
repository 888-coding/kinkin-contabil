# Criação de tabelas
## 1. USUARIOS 
## 2. CONTAS
## 3. MOVIMENTOS 

### SQL para checar se existe tabela: SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'; 

import os 
import sqlite3

nome_arquivo = "contabilidade.db"
if os.path.exists(nome_arquivo):
    # EXISTÊNCIA DO BANCO DE DADOS 
    print("O banco de dados existe")
    conexao = sqlite3.connect('contabilidade.db')
    cursor = conexao.cursor()
    # EXISTÊNCIA DA TABELA DE USUARIOS 
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='usuarios'")
    resultado = cursor.fetchone()
    cursor.close()
    
    if resultado == None:
        print("A tabela não existe")
        cursor = conexao.cursor()
        cursor.execute("CREATE TABLE usuarios (id integer, nome text, senha text)")
        cursor.close()
        print("Foi criado a tabela usuarios neste momento.")    
    else:
        print("A tabela usuarios já existe!") 

    # EXISTÊNCIA DA TABELA CONTAS 
    cursor = conexao.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='contas'")
    resultado = cursor.fetchone()
    cursor.close()

    if resultado == None:
        print("Não tem tabela contas")
        cursor = conexao.cursor()
        cursor.execute("CREATE TABLE contas (contas_id integer PRIMARY KEY AUTOINCREMENT, conta_base text, conta_complementar text, conta_descricao text)")
        cursor.close()
        print("Foi criado a tabela contas neste momento.")
    else:
        print("Tabela contas já existe!")
    
else: 
    print("O banco de dados não existe! ")

