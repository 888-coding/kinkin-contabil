# main.py 
import contas
import movimentacoes
import colorama
from colorama import Fore
def main():
    mostrarMenu()

def mostrarMenu():
    colorama.init()
    print(Fore.GREEN + "====== SISTEMA KINKIN CONTÁBIL =====" + Fore.RESET)
    print(Fore.GREEN + "====================================" + Fore.RESET)
    colorama.deinit()
    print("MENU DO SISTEMA : ------------------")
    print("1 - ACESSAR CONTAS ")
    print("2 - ACESSAR MOVIMENTAÇÕES ")
    print("3 - ACESSAR RELATÓRIOS ")
    print("====================================")
    while True:
        opcao_menu = input("> Escolha uma opção no menu: ")
        if opcao_menu.isdigit():
            if 4 > int(opcao_menu) > 0:
                opcao_menu = int(opcao_menu)
                break
            else:
                print("obs: Escolha a opção certa")
        else:
            print("obs: Escolha a opção certa")

    if opcao_menu == 1:
        print(f"Você escolheu a opção {opcao_menu}")
        contas.acessarContas()
    elif opcao_menu == 2:
        print(f"Você escolheu a opção {opcao_menu}")
        movimentacoes.acessarMovimentacoes()
    else:
        print(f"Você escolheu a opção {opcao_menu}")

main()
