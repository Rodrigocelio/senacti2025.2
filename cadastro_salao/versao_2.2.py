# arquivo: barbearia.py
import json
import urllib.request
from datetime import datetime

def mostrar_menu():
    print("\n=== Sistema de Cadastro de Clientes - Barbearia ===")
    print("1. Cadastrar cliente")
    print("2. Listar clientes")
    print("3. Fazer agendamento")
    print("4. Listar agendamentos")
    print("0. Sair")

def enviar_dados(payload):
    """Envia dados genéricos via webhook."""
    webhook_url = "https://hook.us2.make.com/1adv2sv028glhonhwu3n1mxwzn7dgsp6"  # Substitua pela sua URL do webhook
    headers = {
    "Content-Type": "application/json",
      }
    
    data = json.dumps(payload).encode("utf-8")
 
    requisicao = urllib.request.Request(webhook_url, data=data, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(requisicao) as response:
            status_code = response.getcode()
            if 200 <= status_code < 300:
                print("✅ Dados enviados com sucesso ao webhook!")
            else:
                print(f"⚠️ Erro ao enviar notificação: {status_code}")
    except Exception as e:
        print(f"❌ Falha ao enviar dados: {e}")

def cadastrar_cliente(clientes):
    nome = input("Digite o nome do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    email = input("Digite o email do cliente: ")
    tag = "cadastro"

    cliente = {"nome": nome, "telefone": telefone, "email": email, "tag": tag}
    clientes.append(cliente)
    print(f"\nCliente {nome} cadastrado com sucesso!")
    # Enviar dados do cliente para o webhook
    enviar_dados(cliente)

def listar_clientes(clientes):
    if not clientes:
        print("\n=========================")
        print("Nenhum cliente cadastrado.")
        return
    print("\nLista de clientes cadastrados:")
    for i, cliente in enumerate(clientes, start=1):
        print(f"{i}. Nome: {cliente['nome']}, Telefone: {cliente['telefone']}, Email: {cliente['email']}")

def fazer_agendamento(clientes, agendamentos):
    """Permite listar clientes e agendar um serviço, salvando na memória e enviando via webhook."""
    if not clientes:
        print("\n========================================================")
        print("❌ Nenhum cliente cadastrado. Cadastre antes de agendar.")
        return

    print("\n=== Agendamento de Serviços ===")
    listar_clientes(clientes)

    try:
        print("\n=========================")
        escolha = int(input("Escolha o número do cliente: "))
        if escolha < 1 or escolha > len(clientes):
            print("Cliente inválido.")
            return
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    cliente_selecionado = clientes[escolha - 1]

    # Lista de profissionais
    profissionais = {
        1: "Joao",
        2: "Abraao",
        3: "Rodrigo"
    }

    print("\nProfissionais disponíveis:")
    for id, nome in profissionais.items():
        print(f"{id}. {nome}")
    prof_id = input("Escolha um profissional pelo número: ")
    if prof_id.isdigit() and int(prof_id) in profissionais:
        profissional = profissionais[int(prof_id)]
        print(f"Profissional {profissional} selecionado.")
    else:
        print("Opção de profissional inválida. Tente novamente.")
        return

    # Serviços com descrição e valor
    servicos = {
        1: {"nome": "Corte de cabelo", "descricao": "Corte moderno com acabamento na navalha.", "valor": 30.00},
        2: {"nome": "Barba", "descricao": "Barba desenhada e hidratação com toalha quente.", "valor": 25.00},
        3: {"nome": "Printura", "descricao": "Printura de cabelo com tinta temporária.", "valor": 15.00},
        4: {"nome": "Pacote Completo", "descricao": "Cabelo + Barba + Printura com desconto especial.", "valor": 60.00}
    }

    print("\nServiços disponíveis:")
    for id, info in servicos.items():
        print(f"{id}. {info['nome']} - R${info['valor']:.2f}")
        print(f"   ↳ {info['descricao']}")

    opcao = input("\nEscolha um serviço para agendar: ")
    if opcao.isdigit() and int(opcao) in servicos:
        servico_info = servicos[int(opcao)]
        servico = servico_info["nome"]

        # Solicitar data e horário do agendamento
        data = input("Digite a data do agendamento (DD/MM/YYYY): ")
        hora = input("Digite o horário do agendamento (HH:MM, 24h): ")

        # Validar data e hora
        try:
            dt = datetime.strptime(f"{data} {hora}", "%d/%m/%Y %H:%M")
        except ValueError:
            print("Data ou horário inválidos. Use o formato DD/MM/YYYY e HH:MM.")
            return

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
        agendamentos.append(agendamento)

        # Enviar dados do agendamento para o webhook
        enviar_dados(agendamento)

        print(f"\n✅ Agendamento confirmado para {cliente_selecionado['nome']}: {servico} - R${servico_info['valor']:.2f}")
        print(f"🧔 Profissional: {profissional}")
        print(f"📅 Data: {data} às {hora}")
        print(f"📝 Descrição: {servico_info['descricao']}")
    else:
        print("Opção inválida. Tente novamente.")

def listar_agendamentos(agendamentos):
    """Exibe todos os agendamentos atuais na memória."""
    if not agendamentos:
        print("\n📭 Nenhum agendamento encontrado.")
        return
    print("\n📅 Agendamentos atuais:")
    for i, ag in enumerate(agendamentos, start=1):
        data = ag.get('data', ag.get('datetime', '-')[:10] if ag.get('datetime') else '-')
        hora = ag.get('hora', (ag.get('datetime','')[11:16] if ag.get('datetime') else '-'))
        print(f"{i}. Cliente: {ag['nome']} | Serviço: {ag['servico']} | Profissional: {ag['profissional']} | Valor: R${ag['valor_servico']:.2f} | Data: {data} {hora}")

def main():
    clientes = []
    agendamentos = []

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_cliente(clientes)
        elif opcao == "2":
            listar_clientes(clientes)
        elif opcao == "3":
            fazer_agendamento(clientes, agendamentos)
        elif opcao == "4":
            listar_agendamentos(agendamentos)
        elif opcao == "0":
            print("Saindo do sistema. Até mais! ✂️")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
