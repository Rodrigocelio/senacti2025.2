from os import system
import time


# funcao para exibir o menu
def mostrar_menu():
    """Cria e mostra um menu com as opções possíveis ao usuário."""
    print("\n=== Sistema de Cadastro de Clientes - Barbearia ===")
    print("1. Cadastrar cliente")
    print("2. Listar clientes")
    print("3. Buscar cliente por nome")
    print("4. Sair")


def mostrar_menu():
    """A função mostra um menu com as possivés opções."""
    print("\n==== Sistema de Cadastro de Clientes - Barbearia ====")
    print("1. Cadastrar cliente")
    print("2. Listar clientes")
    print("3. Buscar cliente por nome")
    print("4. Sair\n")


# TODO: Simplificar esse código usando uma função recursiva.
def mostrar_barra_carregamento():
    """Mostra uma barra de carregamento para iniciar o programa."""

    barra = ""
    status = ""

    for i in range(100):
        print("INICIANDO, POR FAVOR AGUARDE.".center(102))
        barra += "/"
        print("."*102)
        print(barra)
        print("."*102)
        status = " " + str(len(barra)) + "% "
        print(status.center(102, "-"))
        time.sleep(.1)
        system("clear")


# TODO: Refazer linhas 56 e 57 com caracteres de escape.
def identificar_opt():
    """Coleta e retorna 'opt'. A opção selecionada pelo usuário."""

    opt_possiveis = (1, 2, 3, 4)

    while True:
        # Busca por entradas inválidas.
        try:
            print("-"*20)
            opt = int(input(">>> "))
            # Verifica se é uma opção válida.
            if opt in opt_possiveis:
                return opt
            raise ValueError
        except ValueError:
            system("clear")
            time.sleep(.1)
            mostrar_menu()
            continue
        except KeyboardInterrupt as erro:
            print("\nEncerando o programa...")
            time.sleep(1.5)
            print("\nPrograma interrupido abruptamente.")
            print("Por favor execute novamente.")
            break


# Execução do programa.
mostrar_barra_carregamento()
mostrar_menu()
identificar_opt()
