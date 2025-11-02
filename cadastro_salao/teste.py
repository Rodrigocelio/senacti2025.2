import getpass
import os


ARQ_CREDENCIAIS = "./senacti2025.2/cadastro_salao/credenciais.txt"


def cadastrar_adm():
    """Cadastra um novo administrador no sistema."""
    if os.path.exists(ARQ_CREDENCIAIS):
        with open(ARQ_CREDENCIAIS, "a") as credenciais:
            usuario, senha = solicitar_login()
            credenciais.write(f"-{usuario}\n")
            credenciais.write(f":{senha}\n\n")
    else:
        raise Exception("Arquivo de credenciais não encontrado!")


def logar(usuario, senha):
    """Verifica se o usuário é um dos adminitradores do sistema. Os valores de 
    login são armazenados em um dicionário que é consultado para validar o 
    acesso.
    """ 
    credenciais = buscar_credenciais_registradas()
    print(credenciais)
    # Valida a credencial informada pelo usuário.
    for i in range(len(credenciais['usuarios'])):
        if usuario == credenciais['usuarios'][i] and senha == credenciais['senhas'][i]:
            print("Ok")
            return 1
    return 0


def buscar_credenciais_registradas():
    """Busca as credenciais armazenadas no arquivo."""
    adm = {'usuarios': [], 'senhas': []}
    try:
        with open(ARQ_CREDENCIAIS) as credenciais:
            for linha in credenciais:
                if linha.startswith("-"):
                    adm['usuarios'].append(linha.removeprefix("-").removesuffix("\n"))
                if linha.startswith(":"):
                    adm['senhas'].append(linha.removeprefix(":").removesuffix("\n"))
    except OSError as erro:
        print(erro)
    return adm


def solicitar_login():
    """Solicita as credenciais do usuário com um diferencial. A senha é 
    solicitada de forma segura, ou seja, ela não é exibida no terminal.
    """
    usuario = input("Usuário: ")
    senha = getpass.getpass("Senha: ", stream=None)
    return usuario, senha

# O simbolo de * serve para indicar que uma tupla será
# desconpactada.
logar(*solicitar_login())
#cadastrar_adm()