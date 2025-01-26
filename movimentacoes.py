#movimentacoes.py
import colorama
from colorama import Fore

def acessarMovimentacoes():
    colorama.init()
    print(Fore.GREEN + ">> MOVIMENTAÇÕES" + Fore.RESET)
    colorama.deinit()
    print("1 - Cadastrar movimentação")
    print("2 - Consultar Movimentação")
    print("3 - Excluir   movimentação")

    while True:
        escolha = input("Escolha a opção : ")
        if escolha.isdigit():
            escolha = int(escolha)
            if (escolha == 1) or (escolha == 2) or (escolha == 3) :
                break
            else:
                print("Erro. Escolha novamente.")
        else:
            print("Erro. Escolha novamente.")
    if escolha == 1:
        cadastrarMovimentacao()
    elif escolha == 2:
        consultarMovimentacao()
    else:
        excluirMovimentacao()

def cadastrarMovimentacao():
    print("Nada1")
def consultarMovimentacao():
    print("Nada2")
def excluirMovimentacao():
    print("Nada3")
