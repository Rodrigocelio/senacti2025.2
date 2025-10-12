# ------ Área de importação
import os
from time import sleep
from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel
from rich.text import Text


# ------ Área de componentes
def limpar_tela():
    """Limpa a tela do console de forma multiplataforma."""
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_menu():
    """A função mostra um menu com as possivés opções."""
    print()
    print("-"*11 + " Sistema de Cadastro de Clientes - Barbearia " + "-"*11)
    print("1. Cadastrar cliente")
    print("2. Listar clientes")
    print("3. Buscar cliente por nome")
    print("4. Sair\n")


def mostrar_titulo_personalizado():
    """Renderiza um texto simples em uma ASCII Art e altera a cor para uma especificada.
    """
    console = Console()
    render = Figlet()
    # Renderiza e cria um painel com o título.
    titulo_renderizado = render.renderText("= BarbeBack =") 
    painel = Panel(titulo_renderizado)
    
    console.print(painel, style="red")
                       

def mostrar_barra_carregamento():
    """Mostra uma barra de carregamento para iniciar o programa."""
    barra = ""

    console = Console()

    for i in range(45):
        mostrar_titulo_personalizado()
        barra += "///"
        # A barra de carregamento será renderizada para a cor verde. 
        painel = Panel.fit(barra, style="green")
        console.print(painel)
        sleep(.1)
        limpar_tela()


def logar(usuario, senha):
    """Verifica se o usuário é um 'adm' do sistema.""" 
    adm = {'usuario': 'salinas', 
           'senha': '123'}

    # Verifica se existe um usuário com o nome especificado
    # caso exista, verifica se a senha está atrelada ao nome especificado.
    if usuario == adm['usuario']:
        if senha == adm['senha']:
            return 1
        return 0


def cadastrar_cliente(clientes):
    """Cadastra um novo cliente.""" 
    print("-"*25, " Cadastrar clinte ", "-"*25)
    nome = input("Nome do cliente: ").lower()
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


def listar_clientes(clientes):
    """Lista todos os clientes utilizando enumerate para contar todos."""
    if not clientes:
        print("Nenhum cliente cadastrado.")
        sleep(3)
        return
    print("")
    print("-"*45, "Lista de clientes cadastrados", "-"*45)

    # Desconpacta o index e os dados do cliente
    for n_cliente, cliente in enumerate(clientes, 1):
        print(f"{n_cliente:>4} -: Nome: {cliente['nome']:<20} | Telefone: {cliente ['telefone']:<20} | Email: {cliente['email']:<20}")


def buscar_clientes(clientes):
    """Busca clientes por nome em uma lista e exibe os resultados."""
    print("-"*67)
    nome_busca = input("Digite o nome do cliente que deseja buscar: ")

    # Filtra a lista de clientes para encontrar nomes que contenham o termo de busca
    resultados = [cliente for cliente in clientes if nome_busca in cliente['nome']]

    print(f"\n--- Resultados da busca por '{nome_busca}' ---")

    if resultados:
        for i, cliente in enumerate(resultados, 1):
            print(f"{i}. Nome: {cliente['nome']}, Telefone: {cliente['telefone']}, Email: {cliente['email']}")
        print("-"*50)
    else:
        print(f"\nNenhum cliente com o nome '{nome_busca}' foi encontrado.")


# ----- Área de execução
def main():
    """Fluxo de execução de todo sistema."""    
    
    clientes = []

    mostrar_barra_carregamento()
    
    # login
    while True:
        mostrar_titulo_personalizado()
        print("-"*30 + " Login " + "-"*30)
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
        mostrar_titulo_personalizado()
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
            mostrar_titulo_personalizado()
            cadastrar_cliente(clientes)
        elif opt == "2":
            limpar_tela()
            mostrar_titulo_personalizado()
            listar_clientes(clientes)
            # Arranjo tecnico para FRISAR a tela na listagem dos clientes
            # caso contrario 'limpar_tela' não deixaria exibir.
            if type(input("\nAperte 'ENTER' para voltar: ")) == str:
                limpar_tela()
                continue
        elif opt == "3":
            limpar_tela()
            mostrar_titulo_personalizado()
            buscar_clientes(clientes)
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
