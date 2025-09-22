import os
from time import sleep

clientes = []

def limpar_tela():
    """Limpa a tela do console de forma multiplataforma."""
    os.system('cls' if os.name == 'nt' else 'clear')


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
    progresso = ""

    for i in range(100):
        print("INICIANDO, POR FAVOR AGUARDE.".center(102))
        barra += "/"
        print("."*102)
        print(barra)
        print("."*102)
        progresso = " " + str(len(barra)) + "% "
        print(progresso.center(102, "-"))
        sleep(.1)
        limpar_tela()


def logar(usuario, senha):
    """Verifica se o usuário é um 'adm' do sistema.""" 
    adm = {'usuario': 'salinas', 
           'senha': '123'}

    # dessa forma fica mais eficiente.
    if usuario == adm['usuario']:
        if senha == adm['senha']:
            return 1
        return 0


def cadastrar_cliente():
    """Cadastra um novo cliente."""
    
    print("="*25, " Cadastrar clinte ", "="*25)
    nome = input("Nome do cliente: ").title()
    telefone = input("Telefone do cliente: ")
    email = input("E-mail do cliente: ").lower()
    
    # Dicionário para o cliente.
    cliente = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    # Adiciona o cliente à lista de clientes cadastrados.
    clientes.append(cliente)
    print(f"\nCliente {nome.capitalize()} cadastrado com sucesso!")


def listar_clientes():
    """Lista todos os clientes com um contador manual."""

    if not clientes:
        print("Nenhum cliente cadastrado.")
        sleep(3)
        return
    print("")
    print("-"*30, "Lista de clientes cadastrados", "-"*30)

    # Desconpacta o index e os dados do cliente
    for n_cliente, cliente in enumerate(clientes):
        # n_cliente é acrescido de 1 porque o index começa em 0.
        print(f"{n_cliente+1} -: Nome: {cliente['nome']} | Telefone: {cliente ['telefone']} | Email: {cliente['email']}")


def main():
    """Fluxo de execução de todo sistema."""
    
    mostrar_barra_carregamento()
    
    # login
    while True:
        print("+"*30 + " Login " + "+"*30)
        usuario = str(input("Usuário: "))
        senha = str(input("Senha: "))
        # verifica se login é válido.
        if logar(usuario, senha) == 1:
            print("\nEntrando...")
            sleep(1)
            limpar_tela()
            break
        else:
            print("""\nUsuário ou senha inválido.
              \nTENTE NOVAMENTE!""")
            limpar_tela()
        
    # loop principal
    while True:
        mostrar_menu()
        print("-"*20)
        try:
            opt = str(input(">>> "))
        # Encerra o programa de forma elegante caso o usuário 
        # tecle 'ctrl + c'.
        except KeyboardInterrupt as erro:
            print("\nEncerando o programa...")
            sleep(1.5)
            print("\nPrograma interrupido abruptamente.")
            print("Por favor execute novamente.")
            break
        if opt == "1":
            limpar_tela()
            cadastrar_cliente()
        elif opt == "2":
            limpar_tela()
            listar_clientes()
            # Arranjo tecnico para FRISAR a tela na listagem dos clientes
            # caso contrario 'limpar_tela' não deixaria exibir.
            if type(input("\nAperte 'ENTER' para voltar: ")) == str:
                limpar_tela()
                continue
        elif opt == "3":
            pass
        elif opt == "4":
            print("\nEncerando o programa...")
            sleep(1.5)
            break
        else:
            print("""Opção inválida!
                  Execute novamente.""")
        limpar_tela()


# Executa o sistema
if __name__ == "__main__":
    main()
