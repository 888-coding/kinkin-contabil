# movimentacoes_cadastrar.py
import colorama
from colorama import Fore

def TelaCadastrarMovimentacoes():
    colorama.init()
    print(Fore.GREEN + "Cadastro de movimentação" + Fore.RESET)
    colorama.deinit()
    # 01 : Data de movimentacao
    # 02 :
    #   02.1 : movimentacoes , passo por passo.
    print("*Para cadastro de movimentacao precisa ter contas cadastradas")
    # Para data de movimentacao precisa eliminar possíveis erros. 
    while True:
        dataMovimentacao = input("Informe a data de cadastro no formato DD/MM/AAAA : ")
        if len(dataMovimentacao) != 10:
            print(Fore.RED + "Favor inserir corretamente!" + Fore.RESET)
        else:
            # 2, 5 = '/'
            if dataMovimentacao[2] != '/' or dataMovimentacao[5] != '/':
                print(Fore.RED + "Favor inserir corretamente!" + Fore.RESET)
            elif dataMovimentacao[0].isdigit() is False:
                print(Fore.RED + "Favor inserir corretamente!" + Fore.RESET)
            elif dataMovimentacao[1].isdigit() is False:
                print(Fore.RED + "Favor inserir corretamente!" + Fore.RESET)
            elif dataMovimentacao[3].isdigit() is False:
                print(Fore.RED + "Favor inserir corretamente!" + Fore.RESET)
            elif dataMovimentacao[4].isdigit() is False:
                print(Fore.RED + "Favor inserir corretamente!" + Fore.RESET)
            elif dataMovimentacao[6].isdigit() is False:
                print(Fore.RED + "Favor inserir corretamente!" + Fore.RESET)
            elif dataMovimentacao[7].isdigit() is False:
                print(Fore.RED + "Favor inserir corretamente!" + Fore.RESET)
            elif dataMovimentacao[8].isdigit() is False:
                print(Fore.RED + "Favor inserir corretamente!" + Fore.RESET)
            elif dataMovimentacao[9].isdigit() is False:
                print(Fore.RED + "Favor inserir corretamente!" + Fore.RESET)
            else:
                break
    return dataMovimentacao
data_movimentacao = TelaCadastrarMovimentacoes()
print(data_movimentacao)


