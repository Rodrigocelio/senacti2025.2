from os import system
import time


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


def logar():
    """Verifica se o usuário é um 'adm' do sistema."""
    
    adm = {'usuario': 'petter', 'senha': '111111'}

    print("#" * 30 + " Login " + "#" * 30)
    usuario = str(input("Usuário: "))
    senha = str(input("Senha: "))

    # dessa forma fica mais eficiente.
    if usuario == adm['usuario']:
        if senha == adm['senha']:
            return 1
    return 0


def main():
    # Execução do programa.
    mostrar_barra_carregamento()

    while True:
        time.sleep(0.5)
        system('clear')
        if logar() == 0:
            print("\nUsuário ou senha inválido.\nTENTE NOVAMENTE!")
            time.sleep(1)
            continue
        print("Entrando...")
        break
    
    time.sleep(1)
    system('clear')
    mostrar_menu()

    identificar_opt()


main()