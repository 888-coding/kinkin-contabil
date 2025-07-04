# contas.py
import sqlite3 as s
from conexao import bancodados_nome
import colorama
from colorama import Fore
import contas_buscar_todos
import contas_cadastro, contas_alterar

def acessarContas():
    colorama.init()
    print(Fore.GREEN + "========== CONTAS =========" + Fore.RESET)
    print(Fore.GREEN + "===========================" + Fore.RESET)
    colorama.deinit()
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

    # 選擇 
    if opcao_menu_contas == 1:
        # 選擇登記
        contas_cadastro.cadastrar()
    elif opcao_menu_contas == 2:
        # 選擇列出全部
        print("Escolheu mostrar todas as contas")
        contas_buscar_todos.mostratodos()
    else:
        # 選擇更改
        print("Escolheu atualizar uma conta")
        contas_alterar.alterar()
    

