# Lista para armazenar os agendamentos
agendamentos = []

#Inserir dados para agendamento
def criar_agendamento():
    """"""
    print("\n --- Novo Agendamento ---")
    try:
        nome = str(input("Nome do Cliente: "))
        telefone = str(input("Telefone: "))
        data = str(input("Data (DD/MM/AAAA): "))
        hora = str(input("Hora (HH:MM): "))
        barbeiro = str(input("Barbeiro responsavel: "))
        servico = str(input("Serviço (ex.corte,barba,...)"))

        #Dicionario do agendamento
        agendamento = {
            "nome": nome,
            "telefone": telefone,
            "data": data,
            "hora": hora,
            "barbeiro": barbeiro,
            "servico": servico}
        agendamentos.append(agendamento)

        print(f"\n ✅ Agendamento confirmado para {nome} em {data} ás {hora} com {barbeiro}.")
    except Exception as erro:
        print(f"Erro ao cadastrar: {erro}")


#lista do agendamentos cadastrado
def listar_agendamentos():
    """"""
    print("\n--- Lista de Agendamentos ---")
    try:
      if not agendamentos:
        print("Nenhum Agendamento Encontrado.")
      else:
        for agendamento, n in enumerate(agendamentos, 1):
          print(f"\n{n}. {agendamento['nome']} - {agendamento['data']} às {agendamento['hora']} | {agendamento['barbeiro']} ({agendamento['servico']})")
    except Exception as erro:
        print(f" Ocorreu um erro ao listar os agendamentos: {erro}")


#Busca agendamento no sistema
def busca_agendamentos():
    """"""
    print(f"\n --- Buscar Agendamentos ---")
    try:
        nome = str(input("Digite nome do cliente: "))

        encontrados = [a for a in agendamentos if a['nome'].lower() == nome.lower()]

        if encontrados:
            for a in encontrados:
                print(f"\ncliente: {a["nome"]}")
                print(f"Telefone: {a["telefone"]}")
                print(f"data: {a["data"]} hora: {a["hora"]}")
                print(f"barbeiro: {a["barbeiro"]}")
                print(f"servico: {a["servico"]}")
        else:
            print("Nenhum agendamento encontrado para esse nome.")
    except Exception as erro:
        print(f" Ocorreu um erro ao buscar agendamento: {erro}")


# Funcão para cancela um agendamento
def cancelar_agendamentos():
  print(f"\n --- Cancelar Agendamento ---")
  try:
      nome = str(input("Digite o nome do cliente: "))
      for i, a in enumerate(agendamentos):
          if a["nome"].lower() == nome.lower():
              cancelado = agendamentos.pop(i)
              print(f'Agendamento com {cancelado['nome']} foi cancelado.')
              return
      print("Agendamento não encontrado.")
  except Exception as erro:
        print(f" Erro ao cancelar: {erro}")