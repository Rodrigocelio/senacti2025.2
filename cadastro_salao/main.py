import os
from time import sleep
import json
import urllib.request
from datetime import datetime
import pyfiglet
from rich.console import Console
from rich.panel import Panel
from rich.text import Text


# Esse é o obejeto da biblioteca Rich que utilizamos para imprimir as 
# informações formatadas.
console = Console()


def limpar_tela():
    """Limpa a tela do console de forma multiplataforma. Essa função funciona 
    para Linux, Mac e Windows.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_logo_personalizado():
    """Cria um logo renderizado pelo módulo pyfiglet e imprime centralizado 
    dentro de um painel definido pela biblioteca Rich. O logo do programa é uma 
    ASCII Art.
    """
    logo = pyfiglet.figlet_format("  BarberBack  ")
    logo_centralizado = Text(logo, justify="center")
    painel = Panel(logo_centralizado)
    console.print(painel, style="white")


def mostrar_barra_carregamento():
    """Mostra uma barra de carregamento. A lógica é simples: temos um laço de 
    um intervalo de 50, a cada volta a variável progresso é incrementada com 
    dois caracteres de barra e no laço seguinte ela é impressa.
    """
    progresso = ""
    for p in range(50):
        mostrar_logo_personalizado()
        progresso_centralizado = Text(progresso, justify="center")
        painel = Panel(progresso_centralizado, title="Carregando, aguarde!")
        console.print(painel, style="white")
        sleep(.1)
        limpar_tela()
        progresso += "//"


def logar(usuario, senha):
    """Verifica se o usuário é um dos adminitradores do sistema. Os valores de 
    login são armazenados em um dicionário que é consultado para validar o 
    acesso.
    """ 
    adm = {'usuario': 'salinas', 
           'senha': '123'}
     
    if usuario == adm['usuario'] and senha == adm['senha']:
            return 1
    return 0


def mostrar_menu():
    """Cria e imprime um menu formatado com a biblioteca Rich."""
    menu = """\n1. Cadastrar cliente\n2. Listar clientes\n3. Buscar cliente por nome\n4. Agendamento\n5. Ver agendamentos\n6. Buscar agendamento\n7. Cancelar agendamento\n8. Sair\n"""

    painel = Panel.fit(menu, title="=== Sistema de Cadastro de Clientes - Barbearia ===")
    console.print(painel, style="white", justify="left")


def enviar_dados(payload):
    """Envia dados genéricos via webhook. A variável 'webhook' é possível 
    atualizar para qualquer outra URL webhook válida.
    """
    webhook_url = "https://hook.us2.make.com/1adv2sv028glhonhwu3n1mxwzn7dgsp6"

    headers = {
    "Content-Type": "application/json",
      }
    
    data = json.dumps(payload).encode("utf-8")
 
    requisicao = urllib.request.Request(webhook_url, data=data, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(requisicao) as response:
            status_code = response.getcode()
            if 200 <= status_code < 300:
                print("\n ✅ Dados enviados com sucesso ao webhook!")
            else:
                print(f"\n ⚠️ Erro ao enviar notificação: {status_code}")
    except Exception as e:
        print(f"\n ❌ Falha ao enviar dados: {e}")


def cadastrar_cliente(clientes):
    """Cadastra um novo cliente armazenando no dicionário 'clientes'."""
    # Cria uma interface mais elegante.
    console.print(Panel("", title="Cadastrar Cliente"), style="white")
    nome = input(" Nome do cliente: ").lower()
    telefone = input(" Telefone do cliente: ")
    email = input(" E-mail do cliente: ").lower().strip()
    tag = "cadastro"
    
    # Dicionário para o cliente.
    cliente = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "tag": tag
    }

    # Adiciona o cliente à lista de clientes cadastrados.
    clientes.append(cliente)
    print(f"\n Cliente {nome.capitalize()} cadastrado com sucesso!")
    enviar_dados(cliente)
    sleep(1)


def listar_clientes(clientes):
    """Lista todos os clientes utilizando enumerate para gerar um ID de 
    cadastro.
    """
    if not clientes:
        print("Nenhum cliente cadastrado.")
        sleep(3)
        return
    
    print("")
    console.print(Panel("", title="Lista de Clientes Cadastrados", style="white"))

    for n, cliente in enumerate(clientes, 1):
        print(f"{n:>4}º -: Nome: {cliente['nome']:<20} | Telefone: {cliente ['telefone']:<20} | Email: {cliente['email']:<20}")


def buscar_clientes(clientes):
    """Busca clientes por nome em uma lista e exibe os resultados."""
    console.print(Panel("", title="Buscar cliente por nome"), style="white")

    nome = str(input(" Digite o nome do cliente que deseja buscar: ")).lower()
    # Filtra a lista de clientes para encontrar nomes que contenham o termo de busca
    resultados = [cliente for cliente in clientes if nome == cliente['nome']]

    console.print(Panel("", title=f"Resultados da busca por '{nome}'", style="white"))

    if resultados:
        for i, cliente in enumerate(resultados, 1):
            print(f"{i:>4}º Nome: {cliente['nome']:<20} Telefone: {cliente['telefone']:<20} Email: {cliente['email']:<20}")
    else:
        print(f"\n Nenhum cliente com o nome '{nome}' foi encontrado.")


def criar_agendamento(clientes, agendamentos, profissionais, servicos):
    """Cria um agendamento de serviço e aciona o envio de e-mail confirmando o 
    agendamento.
    """
    console.print(Panel("", title="Novo Agendamento", style="white"))
    try:
        # Verifica se o cliente já tem cadastro.
        if not clientes:
            print(" ❌ Nenhum cliente cadastrado. Cadastre antes de agendar.")
            return

        listar_clientes(clientes)
        # Coleta o cliente.
        try:
            escolha = int(input("\n\n Escolha o número do cliente: "))
            if escolha < 1 or escolha > len(clientes):
                print(" Cliente inválido!")
                return
        except ValueError:
            print(" Entrada inválida. Digite um número.")
            return
        # Descremento de 1 para alinhar ao comprimento da lista.
        escolha -= 1
        cliente_selecionado = clientes[escolha]

        # Coleta o profissional.
        limpar_tela()
        mostrar_logo_personalizado()
        console.print(Panel("", title="Novo Agendamento", style="white"))
        console.print(Panel("", title="Profissionais disponíveis", style="white"))
        for id, nome in profissionais.items():
            print(f"{id:>4}º -: {nome:<6}")
        prof_id = input("\n\n Escolha um profissional pelo número: ")
        if prof_id.isdigit() and int(prof_id) in profissionais:
            profissional = profissionais[int(prof_id)]
            print(f"\n Profissional {profissional.upper()} selecionado.")
        else:
            print(" Opção de profissional inválida. Tente novamente.")
            return

        # Coleta o serviço.
        limpar_tela()
        mostrar_logo_personalizado()
        console.print(Panel("", title="Novo Agendamento", style="white"))
        console.print(Panel("", title="Serviços disponíveis", style="white"))
        for id, info in servicos.items():
            print(f"{id:>4}º -: {info['nome']:<6} - R${info['valor']:<6.2f} - ↳ {info['descricao']:<6}")

        opcao = input("\n\n Escolha um serviço para agendar: ")
        if opcao.isdigit() and int(opcao) in servicos:
            servico_info = servicos[int(opcao)]
            servico = servico_info["nome"]

        # Coleta a data e hora.
        limpar_tela()
        mostrar_logo_personalizado()
        console.print(Panel("", title="Novo Agendamento", style="white"))
        console.print(Panel("", title="Data/Hora", style="white"))
        try:
            data = input(" Digite a data do agendamento (DD/MM/YYYY): ")
            hora = input(" Digite o horário do agendamento (HH:MM, 24h): ")

            dt = datetime.strptime(f"{data} {hora}", "%d/%m/%Y %H:%M")
        except ValueError:
            print(" Data ou horário inválidos. Use o formato DD/MM/YYYY e HH:MM.")
            return

        # Dicionario do agendamento
        agendamento = {
            "nome": cliente_selecionado["nome"],
            "email": cliente_selecionado["email"],
            "telefone": cliente_selecionado["telefone"],
            "servico": servico,
            "descricao_servico": servico_info["descricao"],
            "valor_servico": servico_info["valor"],
            "profissional": profissional,
            "data": data,
            "hora": hora,
            "datetime": dt.isoformat(),
            "tag": "agendamento"
        }
        
        # Adicionando agendamento a lista de agendados.
        agendamentos.append(agendamento)

        # Enviar dados do agendamento para o webhook
        enviar_dados(agendamento)

        print(f"\n\n ✅ Agendamento confirmado para {cliente_selecionado['nome']}: {servico} - R${servico_info['valor']:.2f}")
        print(f" 🧔 Profissional: {profissional}")
        print(f" 📅 Data: {data} às {hora}")
        print(f" 📝 Descrição: {servico_info['descricao']}")
    except Exception as erro:
        print(f"Erro ao cadastrar: {erro}")


def listar_agendamentos(agendamentos):
    """Lista todos os agendamentos registrados."""
    console.print(Panel("", title="Lista de Agendamentos", style="white"))
    try:
      if not agendamentos:
        print(" Nenhum Agendamento Encontrado.")
      else:
        for i, ag in enumerate(agendamentos, start=1):
            data = ag.get('data', ag.get('datetime', '-')[:10] if ag.get('datetime') else '-')
            hora = ag.get('hora', (ag.get('datetime','')[11:16] if ag.get
            ('datetime') else '-'))

            print(f"{i:>4}º -: Cliente: {ag['nome']:<6} | Serviço: {ag['servico']:<6} | Profissional: {ag['profissional']:<6} | Valor: R${ag['valor_servico']:<6.2f} | Data: {data} - {hora}")
    except Exception as erro:
        print(f" Ocorreu um erro ao listar os agendamentos: {erro}")


def buscar_agendamento(agendamentos):
    """Busca um agendamento especifico dentro de agendamentos."""
    console.print(Panel("", title="Buscar Agendamentos", style="white"))
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
                print(f" Barbeiro: {agendamento["profissional"]}")
                print(f" Servico: {agendamento["servico"]}")
                print(f" Valor[R$]: {agendamento["valor_servico"]:.2f}")
        else:
            print(" Nenhum agendamento encontrado para esse nome.")
    except Exception as erro:
        print(f" Ocorreu um erro ao buscar agendamento: {erro}")


def cancelar_agendamento(agendamentos):
  """Cancela um agendamento informado por um administrador."""
  console.print(Panel("", title="Cancelar Agendamento", style="white"))
  try:
      nome = str(input(" Digite o nome do cliente: "))
      for i, agendamento in enumerate(agendamentos):
          if agendamento["nome"].lower() == nome.lower():
              cancelado = agendamentos.pop(i)
              print(f'\n\n Agendamento com {cancelado['nome']} foi cancelado.')
              return
      print(" Agendamento não encontrado.")
  except Exception as erro:
        print(f" Erro ao cancelar: {erro}")


def main():
    """Fluxo de execução de todo sistema."""    
    profissionais = {
        1: "Joao", 
        2: "Abraao", 
        3: "Rodrigo"
    }
    servicos = {
        1: {"nome": "Corte de cabelo", 
            "descricao": "Corte moderno com acabamento na navalha.", 
            "valor": 30.00},
        2: {"nome": "Barba", 
            "descricao": "Barba desenhada e hidratação com toalha quente.", "valor": 25.00},
        3: {"nome": "Printura", 
            "descricao": "Printura de cabelo com tinta temporária.", 
            "valor": 15.00},
        4: {"nome": "Pacote Completo", 
            "descricao": "Cabelo + Barba + Printura com desconto especial.", "valor": 60.00}
    }
    clientes = []
    agendamentos = []

    mostrar_barra_carregamento()
    
    # login
    while True:
        mostrar_logo_personalizado()
        console.print(Panel("", title="Login", style="white"))
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
            criar_agendamento(clientes, agendamentos, profissionais, servicos)
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
        # Busca um agendamento especifico.
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
