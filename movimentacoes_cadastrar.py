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
    dataMovimentacao = input("Informe a data de cadastro no formato DD/MM/AAAA : ")
    # Para data de movimentacao precisa eliminar possíveis erros. 
TelaCadastrarMovimentacoes()