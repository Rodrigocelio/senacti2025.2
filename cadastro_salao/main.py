from funcionalidades import *
from os import system
import time


def main():
    """Fluxo de execução de todo sistema."""
    
    mostrar_barra_carregamento()
    logar()

    while True:
        system('clear')
        mostrar_menu()
        opt = identificar_opt()
        if opt == 1:
            cadastrar_cliente()
        elif opt == 2:
            listar_clientes()
            if type(input("\nDigite quelquer tecla para voltar ao menu: ")) == str(""):
                continue        
        elif opt == 3:
            pass
        elif opt == 4:
            break
        else:
            pass


main()