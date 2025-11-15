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


def validar_email(email):
    """Valida por meio de uma expressão regular simples se o e-mail está no formato correto. Essa implementação serve para evitar que o webhook não engasgue caso o usuário entre um e-mail errado..
    """
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email) is not None
