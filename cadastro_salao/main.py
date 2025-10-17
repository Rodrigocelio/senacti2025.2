import os
from time import sleep
import pyfiglet
from rich.console import Console
from rich.panel import Panel
from rich.text import Text


console = Console()


def limpar_tela():
    """Limpa a tela do console de forma multiplataforma."""
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_logo_personalizado():
    """Renderiza a logo do programa em uma ASCII Art."""
    logo = pyfiglet.figlet_format("  BarbeBack  ")
    logo_centralizado = Text(logo, justify="center")
    painel = Panel(logo_centralizado)
    console.print(painel, style="gray30")


def mostrar_barra_carregamento():
    """Mostra uma barra de carregamento para iniciar o programa."""
    progresso = ""
    for p in range(50):
        mostrar_logo_personalizado()
        # Centraliza a barra, coloca no painel e mostra o painel.
        progresso_centralizado = Text(progresso, justify="center")
        painel = Panel(progresso_centralizado, title="Carregando, aguarde!")
        console.print(painel, style="gray30")
        sleep(.1)
        limpar_tela()
        progresso += "//"


def logar(usuario, senha):
    """Verifica se o usuário é um 'adm' do sistema.""" 
    # Armazena o usuário e senha capaz de logar no sistema.
    adm = {'usuario': 'salinas', 
           'senha': '123'}
    # Verifica se existe o usuário está cadastrado. 
    if usuario == adm['usuario'] and senha == adm['senha']:
            return 1
    return 0


def mostrar_menu():
    """A função mostra um menu com as possivés opções."""
    menu = """\n1. Cadastrar cliente\n2. Listar clientes\n3. Buscar cliente por nome\n4. Agendamento\n5. Ver agendamentos\n6. Buscar agendamento\n7. Cancelar agendamento\n8. Sair\n"""
    # Cria um painel com uma saida mais elegante.
    painel = Panel.fit(menu, title="=== Sistema de Cadastro de Clientes - Barbearia ===")
    console.print(painel, style="gray30", justify="left")


# Adicionar tratamento de exceções.
def cadastrar_cliente(clientes):
    """Cadastra um novo cliente.""" 
    console.print(Panel("", title="Cadastrar Cliente"), style="gray30")
    nome = input(" Nome do cliente: ").lower()
    telefone = input(" Telefone do cliente: ")
    email = input(" E-mail do cliente: ").lower()
    
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
    console.print(Panel("", title="Lista de Clientes Cadastrados", style="gray30"))

    # Desconpacta o index e os dados do cliente
    for n, cliente in enumerate(clientes, 1):
        print(f"{n:>4}º -: Nome: {cliente['nome']:<20} | Telefone: {cliente ['telefone']:<20} | Email: {cliente['email']:<20}")


def buscar_clientes(clientes):
    """Busca clientes por nome em uma lista e exibe os resultados."""
    console.print(Panel("", title="Buscar cliente por nome"), style="gray30")
    nome_busca = str(input(" Digite o nome do cliente que deseja buscar: ")).lower()
    # Filtra a lista de clientes para encontrar nomes que contenham o termo de busca
    resultados = [cliente for cliente in clientes if nome_busca == cliente['nome']]

    console.print(Panel("", title=f"--- Resultados da busca por '{nome_busca}' ---", style="gray30"))

    if resultados:
        for i, cliente in enumerate(resultados, 1):
            print(f"{i:>4}º Nome: {cliente['nome']:<20} Telefone: {cliente['telefone']:<20} Email: {cliente['email']:<20}")
        console.print(Panel("", style="gray30"))
    else:
        print(f"\n Nenhum cliente com o nome '{nome_busca}' foi encontrado.")


# TODO: A função deverá verificar o usuário já está cadastrado.
def criar_agendamento(agendamentos):
    """Cria um agendamento de serviço."""
    console.print(Panel("", title="Novo Agendamento", style="gray30"))
    try:
        nome = str(input(" Nome do Cliente: "))
        telefone = str(input(" Telefone: "))
        data = str(input(" Data[dd/mm/aa]): "))
        hora = str(input(" Hora[hh:mm]: "))
        barbeiro = str(input(" Barbeiro responsavel: "))
        servico = str(input(" Serviço[ex.corte, barba)]: "))

        # Formatando os dados.
        #Dicionario do agendamento
        agendamento = {
            "nome": nome,
            "telefone": telefone,
            "data": data,
            "hora": hora,
            "barbeiro": barbeiro,
            "servico": servico}
        
        # Adicionando agendamento a lista de agendados.
        agendamentos.append(agendamento)

        print(f"\n ✅ Agendamento confirmado para {nome} em {data} ás {hora} com {barbeiro}.")
    except Exception as erro:
        print(f"Erro ao cadastrar: {erro}")


def listar_agendamentos(agendamentos):
    """Lista todos os agendamentos registrados."""
    console.print(Panel("", title="Lista de Agendamentos", style="gray30"))
    try:
      if not agendamentos:
        print(" Nenhum Agendamento Encontrado.")
      else:
        for n, agendamento in enumerate(agendamentos, 1):
          print(f"{n:>4}º {agendamento['nome']:<20} | {agendamento['data']:<20} | {agendamento['hora']:<20} | {agendamento['barbeiro']:<20} [{agendamento['servico']:<20}]")
    except Exception as erro:
        print(f" Ocorreu um erro ao listar os agendamentos: {erro}")


def buscar_agendamento(agendamentos):
    """Busca um agendamento especifico dentro de agendamentos."""
    console.print(Panel("", title="Buscar Agendamentos", style="gray30"))
    try:
        nome = str(input(" Digite nome do cliente: "))
        # Lista de compreesão para localizar o nome na lista de clientes.
        encontrados = [agendamento for agendamento in agendamentos if agendamento['nome'].lower() == nome.lower()]
        if encontrados:
            for agendamento in encontrados:
                print(f"\n Cliente: {agendamento["nome"]}")
                print(f" Telefone: {agendamento["telefone"]}")
                print(f" Data: {agendamento["data"]}")
                print(f" Hora: {agendamento["hora"]}")
                print(f" Barbeiro: {agendamento["barbeiro"]}")
                print(f" Servico: {agendamento["servico"]}")
        else:
            print(" Nenhum agendamento encontrado para esse nome.")
    except Exception as erro:
        print(f" Ocorreu um erro ao buscar agendamento: {erro}")


def cancelar_agendamento(agendamentos):
  """Cancela um agendamento especifico."""
  console.print(Panel("", title="Cancelar Agendamento", style="gray30"))
  try:
      nome = str(input("Digite o nome do cliente: "))
      for i, agendamento in enumerate(agendamentos):
          if agendamento["nome"].lower() == nome.lower():
              cancelado = agendamentos.pop(i)
              print(f'\n\nAgendamento com {cancelado['nome']} foi cancelado.')
              return
      print(" Agendamento não encontrado.")
  except Exception as erro:
        print(f" Erro ao cancelar: {erro}")


def main():
    """Fluxo de execução de todo sistema."""    

    # Estrutura onde ficam armazenados os dados dos clientes.
    clientes = []
    agendamentos = []

    mostrar_barra_carregamento()
    
    # login
    while True:
        mostrar_logo_personalizado()
        console.print(Panel("", title="Login", style="gray30"))
        usuario = str(input(" Usuário: "))
        senha = str(input(" Senha: "))
        # verifica se login é válido.
        if logar(usuario, senha) == 1:
            print("\n Entrando...")
            sleep(1)
            limpar_tela()
            break
        else:
            print("""\nUsuário ou senha inválido.
              \nTENTE NOVAMENTE!""")
            limpar_tela()
        
    # loop principal
    while True:
        mostrar_logo_personalizado()
        mostrar_menu()
        #console.print("-"*13, style="red")
        try:
            opt = str(input(" >>> "))
        # Encerra o programa de forma elegante caso o usuário 
        # tecle 'ctrl + c'.
        except KeyboardInterrupt:
            print("\n Encerando o programa...")
            sleep(1.5)
            print("\n Programa interrupido abruptamente.")
            print(" Por favor execute novamente.")
            break
        # Abre a telinha para cadastrar cliente.
        if opt == "1":
            limpar_tela()
            mostrar_logo_personalizado()
            cadastrar_cliente(clientes)
        # Mostra um relatório com todos os clientes cadastrados.
        elif opt == "2":
            limpar_tela()
            mostrar_logo_personalizado()
            listar_clientes(clientes)
            # Congela a tela até que o usuário digite alguma coisa.
            if type(input("\n\n\n Aperte 'ENTER' para voltar: ")) == str:
                limpar_tela()
                continue
        # Abre a telinha para buscar um cliente especifico.
        elif opt == "3":
            limpar_tela()
            mostrar_logo_personalizado()
            buscar_clientes(clientes)
            # Congela a tela até que o usuário digite alguma coisa
            if type(input("\n\n\n Aperte 'ENTER' para voltar: ")) == str:
                limpar_tela()
                continue
        # Abre uma tela para criar um agendamento.
        elif opt == "4":
            limpar_tela()
            mostrar_logo_personalizado()
            criar_agendamento(agendamentos)
            sleep(3)
        # Mostra todos os agendamentos.
        elif opt == "5":
            limpar_tela()
            mostrar_logo_personalizado()
            listar_agendamentos(agendamentos)
            # Congela a tela até que o usuário digite alguma coisa
            if type(input("\n\n\n Aperte 'ENTER' para voltar: ")) == str:
                limpar_tela()
                continue
        # BIsca um agendamento especifico.
        elif opt == "6":
            limpar_tela()
            mostrar_logo_personalizado()
            buscar_agendamento(agendamentos)
            # Congela a tela até que o usuário digite alguma coisa
            if type(input("\n\n\n Aperte 'ENTER' para voltar: ")) == str:
                limpar_tela()
                continue
        # Cencela um agendamento.
        elif opt == "7":
            limpar_tela()
            mostrar_logo_personalizado()
            cancelar_agendamento(agendamentos)
            # Congela a tela até que o usuário digite alguma coisa
            if type(input("\n\n\n Aperte 'ENTER' para voltar: ")) == str:
                limpar_tela()
                continue
        # Encerra o programa.
        elif opt == "8":
            print("\n Encerando o programa...")
            sleep(1.5)
            break
        else:
            # escrever o else corretamente.
            pass
        limpar_tela()


# Executa o sistema
if __name__ == "__main__":
    main()
