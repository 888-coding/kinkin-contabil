# Criação de Banco de dados 
# - Fazer condição para não ter duplicidade
# - Nome do banco de dados : contabilidade.db 


import os

nome_arquivo = "contabilidade.db"

if os.path.exists(nome_arquivo):
    print("O arquivo existe")
else:
    print("Não existe arquivo")
    # Criação de banco de dados


