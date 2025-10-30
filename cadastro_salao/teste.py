import getpass


def logar(user, password):
    """Verifica se o usuário é um dos adminitradores do sistema. Os valores de 
    login são armazenados em um dicionário que é consultado para validar o 
    acesso.
    """ 
    adm = {'usuario': '', 
           'senha': ''}

    try:
        with open("./senacti2025.2/cadastro_salao/credenciais.txt") as credenciais:
            for linha in credenciais:
                # captura o nome de usuário.
                if linha.startswith("-"):
                    usuario = linha.removeprefix("-")
                    usuario = usuario.removesuffix("\n")
                    adm["usuario"] = usuario
                # captura a senha.
                if linha.startswith(":"):
                    senha = linha.removeprefix(":")
                    senha = senha.removesuffix("\n")
                    adm["senha"] = senha
    except OSError as erro:
        print(erro)
    else:
        # Valida a credencial informada pelo usuário.
        if user == adm['usuario'] and password == adm['senha']:
                print("OK")


def solicitar_login():
    """Solicita as credenciais do usuário com um diferencial. A senha é 
    solicitada de forma segura, ou seja, ela não é exibida no terminal.
    """
    usuario = input("Usuário: ")
    senha = getpass.getpass("Senha: ", stream=None)
    logar(usuario, senha)


solicitar_login()