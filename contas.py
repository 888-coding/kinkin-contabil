# contas.py
import sqlite3 as s
from conexao import bancodados_nome 

def acessarContas():
    print("========== CONTAS =========")
    print("===========================")
    print("1. Cadastrar uma conta.")
    print("2. Mostrar todas as contas.")
    print("3. Atualizar uma conta.")
    print("===========================")
    while True:
        opcao_menu_contas = input("> Escolha uma opção : ")
        if opcao_menu_contas.isdigit():
            opcao_menu_contas = int(opcao_menu_contas)
            if opcao_menu_contas < 4 and opcao_menu_contas > 0 :
                break
            else:
                print("obs: Escolha uma opção correta!")
        else:
            print("obs: Escolha uma opção correta!")

    # Escolheu uma opção 
    if opcao_menu_contas == 1:
        print("Escolheu cadastra uma conta")
                    
    elif opcao_menu_contas == 2:
        print("Escolheu mostrar todas as contas")
        conexao = s.connect(bancodados_nome)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM contas")
        resultados = cursor.fetchall()
        if resultados == None:
            print("Não existe cadastro.")
        else:
            print(resultados)
        conexao.close()

        #print(resultados)        
    else:
        print("Escolheu atualizar uma conta")
    

