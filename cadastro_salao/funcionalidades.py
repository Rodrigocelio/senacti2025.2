from os import system
import time

clientes = []

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

    while True:
        time.sleep(0.5)
        system('clear')
        print("#" * 30 + " Login " + "#" * 30)
        usuario = str(input("Usuário: "))
        senha = str(input("Senha: "))

        # dessa forma fica mais eficiente.
        if usuario == adm['usuario']:
            if senha == adm['senha']:
                print("\nEntrando...")
                time.sleep(1)
                system('clear')
                break
        print("\nUsuário ou senha inválido.\nTENTE NOVAMENTE!")


def cadastrar_cliente():
    """Cadastra um novo cliente."""
    
    system('clear')
    
    nome = input("Digite o nome do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    email = input("Digite o email do cliente: ")
    # Dicionário para o cliente.
    cliente = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    # Adiciona o cliente à lista de clientes cadastrados.
    clientes.append(cliente)
    print(f"Cliente {nome} cadastrado com sucesso!")


def listar_clientes():
    """Lista todos os clientes com um contador manual."""
    
    system('clear')

    if not clientes:
        print("Nenhum cliente cadastrado.")
        time.sleep(3)
        return
    print("")
    print("-"*30, "Lista de clientes cadastrados", "-"*30)

    # Desconpacta o index e os dados do cliente
    for n_cliente, cliente in enumerate(clientes):
        # n_cliente é acrescido de 1 porque o index começa em 0.
        print(f"""{n_cliente+1}. 
              Nome: {cliente['nome']}, 
              Telefone: {cliente ['telefone']}, 
              Email: {cliente['email']}""")
