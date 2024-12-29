# main.py 


def main():
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
                print("Escolha a opção certa: ")
        else:
            print("Escolha a opção certa: ")

    print(f"A Opção escolhida foi : {opcao_menu}")

main()