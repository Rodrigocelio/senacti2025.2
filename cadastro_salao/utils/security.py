def _carregar_ou_gerar_chave(arq_chave: str) -> bytes:
    """Carrega a chave do arquivo ou gera uma nova e salva em arq_chave."""
    try:
        with open(arq_chave, "rb") as arq_chave:
            return arq_chave.read()
    except FileNotFoundError:
        chave = Fernet.generate_key()
        # gravação com permissão restrita (onde suportado)
        with open(arq_chave, "wb") as arq_chave:
            arq_chave.write(chave)
            return chave
        

def _criptografar_credenciais(usuario, senha) -> bytes:
    """"""
    try:
        usuario_cripto = fernet.encrypt(usuario.encode())
        senha_cripto = fernet.encrypt(senha.encode())
    except Exception as erro:
        raise Exception("Erro desconhecido!")
    return usuario_cripto, senha_cripto


def _descriptografar_credenciais(credenciais: bytes) -> str:
    """"""
    try:
        credenciais_descripto = fernet.decrypt(credenciais)
    except Exception as erro:
        raise Exception("Erro desconhecido!")
    return credenciais_descripto


def cadastrar_adm():
    """Cadastra um novo administrador no sistema."""
    if os.path.exists(ARQ_CREDENCIAIS):
        usuario, senha = solicitar_login()
        # Formatando usuario e senha para gravar no arquivo.
        usuario = f"-{usuario}\n"
        senha = f":{senha}\n\n"
        
        with open(ARQ_CREDENCIAIS, "a") as credenciais:        
            usuario_cripto, senha_cripto = _criptografar_credenciais(usuario, senha)

            # Convertemos os bytes criptografados em base64, ou seja, texto 
            # ASCII que pode ser escrito no arquivo.
            b64_usuario = base64.b64encode(usuario_cripto).decode()
            b64_senha = base64.b64encode(senha_cripto).decode()

            # Escreve o texto referente ao usuário e senha no arquivo.
            # grava cada token em sua própria linha (facilita a leitura)
            credenciais.write(b64_usuario + "\n")
            credenciais.write(b64_senha + "\n")


def buscar_credenciais_registradas():
    adm = {'usuarios': [], 'senhas': []}
    try:
        if not os.path.exists(ARQ_CREDENCIAIS):
            return adm

        with open(ARQ_CREDENCIAIS, 'r') as credenciais:
            for linha_pura in credenciais:
                linha = linha_pura.strip()
                if not linha:
                    continue
                try:
                    # cada linha é um token base64 separado
                    token = base64.b64decode(linha)
                except Exception:
                    # formato inválido; pula
                    continue

                try:
                    cred_descriptografadas = _descriptografar_credenciais(token)
                except Exception:
                    # não consegue descriptografar esse token (chave errada / dado corrompido)
                    # pula e continua
                    continue

                try:
                    texto_credenciais = cred_descriptografadas.decode()
                except Exception:
                    continue

                # O texto pode conter múltiplas linhas; processa cada uma
                for linha in texto_credenciais.splitlines():
                    if linha.startswith("-"):
                        adm['usuarios'].append(linha.removeprefix("-"))
                    elif linha.startswith(":"):
                        adm['senhas'].append(linha.removeprefix(":"))
    except OSError as erro:
        print(f"Erro desconhecido: {erro}")
    return adm


def logar():
    """Verifica se o usuário é um dos adminitradores do sistema. Os valores de 
    login estão em um dicionário que é consultado para validar o acesso.
    """ 
    adm = buscar_credenciais_registradas()
    usuario, senha = solicitar_login()
    for par_credencial in zip(adm['usuarios'], adm['senhas']):
        if usuario == par_credencial[0] and senha == par_credencial[1]:
            return 1
    return 0
