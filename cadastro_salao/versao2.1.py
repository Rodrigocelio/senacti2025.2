## Sistema de Cadastro de Clientes para Barbearia

def mostrar_menu():
    """Mostra o menu principal do sistema."""
    print("\n=== Sistema de Cadastro de Clientes - Barbearia ===")
    print("1. Cadastrar cliente")
    print("2. Listar clientes")
    print("3. Agendar serviços ")
    print("4. Buscar clientes")
    print("0. Sair")

def cadastrar_cliente(clientes):
    """Cadastra um novo cliente."""
    nome = input("Digite o nome do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    email = input("Digite o email do cliente: ")
    """Dicionário para o cliente."""
    cliente = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    """Adiciona o cliente à lista de clientes cadastrados."""
    clientes.append(cliente)
    print(f"Cliente {nome} cadastrado com sucesso!")

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
        
def buscar_clientes(clientes):

    """  Busca clientes por nome em uma lista e exibe os resultados. """
    nome_busca = input("Digite o nome do cliente que deseja buscar: ")

    """Filtra a lista de clientes para encontrar nomes que contenham o termo de busca"""
    resultados = [cliente for cliente in clientes if nome_busca.lower() in cliente['nome'].lower()]

    print(f"\n--- Resultados da busca por '{nome_busca}' ---")

    if resultados:
        for i, cliente in enumerate(resultados, 1):
            print(f"{i}. Nome: {cliente['nome']}, Telefone: {cliente['telefone']}, Email: {cliente['email']}")
        print("------------------------------------------")
    else:
        print(f"\nNenhum cliente com o nome '{nome_busca}' foi encontrado.")

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
        elif opcao == "4":
            buscar_clientes(clientes)
        elif opcao == "0":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

## Executa o sistema
if __name__ == "__main__":
    main()