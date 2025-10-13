## Sistema de Cadastro de Clientes para Barbearia

# Importação de bibliotecas necessárias
import json
import urllib.request

def mostrar_menu():
    """Mostra o menu principal do sistema."""
    print("\n=== Sistema de Cadastro de Clientes - Barbearia ===")
    print("1. Cadastrar cliente")
    print("2. Listar clientes")
    print("0. Sair")


def enviar_dados(cliente):
    """Envia as informações do cliente via webhook usando apenas bibliotecas padrão."""
    webhook_url = "https://hook.us2.make.com/1adv2sv028glhonhwu3n1mxwzn7dgsp6"

    data = json.dumps(cliente).encode("utf-8")  # converte o dicionário para bytes JSON
    headers = {"Content-Type": "application/json"}

    """ Cria a requisição HTTP POST """
    requisicao = urllib.request.Request(
        webhook_url,
        data=data,
        headers=headers,
        method="POST"
    )

    try:
        with urllib.request.urlopen(requisicao) as response:
            status_code = response.getcode()
            if 200 <= status_code < 300:
                print(f"✅ Informações de cadastro enviadas pra o email {cliente['email']}!")
            else:
                print(f"⚠️ Erro ao enviar notificação: {status_code}")
    except Exception as e:
        print(f"❌ Falha ao enviar notificação: {e}")

def cadastrar_cliente(clientes):
    """Cadastra um novo cliente."""
    nome = input("Digite o nome do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    email = input("Digite o email do cliente: ")
    tag = "agendamento"
    """Dicionário para o cliente."""
    cliente = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "tag": tag
    }
    """Adiciona o cliente à lista de clientes cadastrados."""
    clientes.append(cliente)
    print('-----------------------------------------------')
    print(f"Cliente {nome} cadastrado com sucesso!")
    print('-----------------------------------------------')

    """Envia os dados do cliente via webhook."""
    enviar_dados(cliente)

def listar_clientes(clientes):
    """Lista todos os clientes com um contador manual."""
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    print("\nLista de clientes cadastrados:")

    """ 1. Inicializa o contador antes do laço """
    numero_cliente = 1

    """ 2. Faz um laço simples pela lista de clientes """
    for cliente in clientes:
        """ 3. Usa a variável do contador no print """
        print(f"{numero_cliente}. Nome: {cliente['nome']}, Telefone: {cliente['telefone']}, Email: {cliente['email']}")

        """ 4. Incrementa o contador para a próxima volta """
        numero_cliente += 1


def main():
    """Função principal do sistema."""
    clientes = [] 
    while True: 
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_cliente(clientes)
        elif opcao == "2":
            listar_clientes(clientes)
        elif opcao == "0":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

## Executa o sistema
if __name__ == "__main__":
    main()