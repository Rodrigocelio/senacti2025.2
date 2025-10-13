# arquivo: barbearia.py
import json
import urllib.request

def mostrar_menu():
    print("\n=== Sistema de Cadastro de Clientes - Barbearia ===")
    print("1. Cadastrar cliente")
    print("2. Listar clientes")
    print("3. Fazer agendamento")
    print("4. Listar agendamentos")
    print("0. Sair")

def enviar_dados(payload):
    """Envia dados genéricos via webhook."""
    webhook_url = "https://projectosenac.free.beeceptor.com"
    data = json.dumps(payload).encode("utf-8")
    headers = {"Content-Type": "application/json"}
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

    servicos = {
        1: "Corte de cabelo",
        2: "Barba",
        3: "Sobrancelha",
        4: "Pacote Completo"
    }

    print("\nServiços disponíveis:")
    for id, nome in servicos.items():
        print(f"{id}. {nome}")

    opcao = input("Escolha um serviço para agendar: ")
    if opcao.isdigit() and int(opcao) in servicos:
        servico = servicos[int(opcao)]
        agendamento = {
            "cliente": cliente_selecionado["nome"],
            "email": cliente_selecionado["email"],
            "telefone": cliente_selecionado["telefone"],
            "servico": servico,
            "tag": "agendamento"
        }
        agendamentos.append(agendamento)
        enviar_dados(agendamento)
        print(f"\n✅ Agendamento confirmado para {cliente_selecionado['nome']}: {servico}")
    else:
        print("Opção inválida. Tente novamente.")

def listar_agendamentos(agendamentos):
    """Exibe todos os agendamentos atuais na memória."""
    if not agendamentos:
        print("\n📭 Nenhum agendamento encontrado.")
        return
    print("\n📅 Agendamentos atuais:")
    for i, ag in enumerate(agendamentos, start=1):
        print(f"{i}. Cliente: {ag['cliente']} | Serviço: {ag['servico']} | Email: {ag['email']}")

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
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
