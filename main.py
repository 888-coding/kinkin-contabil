# main.py 
import contas

def main():
    mostrarMenu()

def mostrarMenu():
    print("====== SISTEMA KINKIN CONTÁBIL =====")
    print("====================================")
    print("MENU DO SISTEMA : ------------------")
    print("1 - ACESSAR CONTAS ")
    print("2 - ACESSAR MOVIMENTAÇÕES ")
    print("3 - ACESSAR RELATÓRIOS ")
    print("====================================")
    while True:
        opcao_menu = input("> Escolha uma opção no menu: ")
        if opcao_menu.isdigit():
            if int(opcao_menu) < 4 and int(opcao_menu) > 0 :
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
    else:
        print(f"Você escolheu a opção {opcao_menu}")

def acessarContas():
    print("Você está dentro da função acessarConta!")

main()