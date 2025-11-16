from time import sleep
from rich.console import Console
from datetime import datetime
from rich.panel import Panel

from core.web_integration import (enviar_dados, validar_email)
from utils.console_tools import (limpar_tela, mostrar_logo_personalizado)


console = Console()


def cadastrar_cliente(clientes):
    """Cadastra um novo cliente armazenando no dicionário 'clientes'."""
    # Cria uma interface mais elegante.
    titulo = "Cadastrar Cliente"
    console.print(Panel("", title=titulo), style="white")

    nome = str(input(" Nome do cliente: ")).lower().strip()
    telefone = str(input(" Telefone do cliente: ")).strip()

    while True:
        email = str(input(" E-mail do cliente: ")).lower().strip()
        if validar_email(email):
            break
        print("E-mail inválido, tente novamente.")
    
    tag = "cadastro"
    
    # Armazenando dados do cliente.
    cliente = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "tag": tag
    }

    # Adiciona o cliente à lista de clientes.
    clientes.append(cliente)
    console.print(f"\n Cliente {nome.capitalize()} cadastrado com sucesso!")
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
    titulo = "Lista de Clientes Cadastrados"
    console.print(Panel("", title=titulo, style="white"))

    for n, cliente in enumerate(clientes, 1):
        console.print(f"{n:>4}º -: Nome: {cliente['nome']:<20} | Telefone: {cliente ['telefone']:<20} | Email: {cliente['email']:<20}",style="red")


def buscar_clientes(clientes):
    """Busca clientes por nome em uma lista e exibe os resultados."""
    titulo = "Buscar cliente por nome"
    console.print(Panel("", title=titulo), style="white")

    nome = str(input(" Nome do cliente que deseja buscar: ")).lower().strip()
    # Encontra nomes que contenham o termo de busca
    encontrado = [cliente for cliente in clientes if nome == cliente['nome']]

    console.print(Panel("", title=f"Resultados da busca por '{nome}'", style="white"))

    if encontrado:
        for i, cliente in enumerate(encontrado, 1):
            console.print(f"{i:>4}º Nome: {cliente['nome']:<20} Telefone: {cliente['telefone']:<20} Email: {cliente['email']:<20}")
    else:
        console.print(f"\n Nenhum cliente com o nome '{nome}' foi encontrado.")


def _selecionar_cliente(clientes):
    """"""
    # Coleta o cliente.
    try:
        id_cliente = int(input("\n\n Escolha o ID do cliente: "))
        if id_cliente < 1 or id_cliente > len(clientes):
            print(" Cliente inválido!")
            return
    except ValueError:
        print(" Entrada inválida, digite um número.")
        return
    # Descremento de 1 para alinhar ao comprimento da lista.
    id_cliente -= 1
    return clientes[id_cliente]


def _selecionar_profisional(profissionais):
    """"""
    limpar_tela()
    mostrar_logo_personalizado()
    console.print(Panel("", title="Novo Agendamento", style="white"))
    titulo = "Profissionais disponíveis"
    console.print(Panel("", title=titulo, style="white"))
    
    for id, nome in profissionais.items():
        print(f"{id:>4}º -: {nome:<6}")

    prof_id = str(input("\n\n Escolha o ID do profissional: ")).strip()
    if prof_id.isdigit() and int(prof_id) in profissionais:
        profissional = profissionais[int(prof_id)]
        print(f"\n Profissional {profissional.capitalize()} selecionado.")
    else:
        print(" Opção de profissional inválida. Tente novamente.")
        return
    return profissional


def _selecionar_servico(servicos):
    """"""
    limpar_tela()
    mostrar_logo_personalizado()
    console.print(Panel("", title="Novo Agendamento", style="white"))
    console.print(Panel("", title="Serviços disponíveis", style="white"))

    for id, info in servicos.items():
        print(f"{id:>4}º -: {info['nome']:<6} - R${info['valor']:<6.2f} - ↳ {info['descricao']:<6}")

    opcao = input("\n\n Escolha o ID do serviço: ")
    if opcao.isdigit() and int(opcao) in servicos:
        servico_info = servicos[int(opcao)]
        servico = servico_info["nome"]
    return (servico, servico_info)


def _coletar_timestamp():
    """"""
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
    return (data, hora, dt)


def criar_agendamento(clientes, agendamentos, profissionais, servicos):
    """Cria um agendamento de serviço e aciona o envio de e-mail confirmando o 
    agendamento.
    """
    console.print(Panel("", title="Novo Agendamento", style="white"))

    try:
        # Verifica se existe clientes cadastros.
        if not clientes:
            print(" ❌ Nenhum cliente cadastrado. Cadastre antes de agendar.")
            return
        listar_clientes(clientes)

        # Área de coleta do cliente.
        cliente_selecionado = _selecionar_cliente(clientes)

        # Área de coleta do profissional.
        profissional = _selecionar_profisional(profissionais)

        # Área de coleta do serviço.
        servico, servico_info = _selecionar_servico(servicos)

        # Área de coleta da data e hora.
        data, hora, dt = _coletar_timestamp()

        # Armazenamento do agendamento.
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
        
        # Registrando agendamento.
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
    titulo = "Lista de Agendamentos"
    console.print(Panel("", title=titulo, style="white"))
    try:
        if not agendamentos:
            print(" Nenhum Agendamento Encontrado.")
            return
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
