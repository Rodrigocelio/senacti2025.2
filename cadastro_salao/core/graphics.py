import os
from os.path import join, dirname
import io
import base64
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


AGENDAMENTOS = join(dirname(__file__), "..", "data", "agendamentos.xlsx")


def gerar_grafico_servico_mais_procurado():
    """Gerar o gráfico de serviço mais procurado. Um gráfico de barras que é 
    alimentado pela contagem da coluna 'servico' da planilha de agendamentos.
    Esse gráfico é salvo em um buffer de memória e convertido para uma 
    representação em base64, que é retornada para ser exibida na página HTML.
    """
    try:
        if not os.path.exists(AGENDAMENTOS):
            return []
        
        df = pd.read_excel(AGENDAMENTOS, sheet_name="agendamentos")
        
        servico_mais_procurado = df['servico'].value_counts()
    
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.barplot(x=servico_mais_procurado.index, y=servico_mais_procurado.values, palette="viridis", ax=ax)
        ax.set_title('Serviço Mais Procurado')
        ax.set_xlabel('Serviços')
        ax.set_ylabel('Quantidade')
        
        # Salvando imagem do gráfico no buffer de memória.
        imagem = io.BytesIO()
        fig.savefig(imagem, format="png")
        imagem.seek(0)

        # Criando uma representação ASCII para o HTML.
        imagem_url = base64.b64encode(imagem.getvalue()).decode()

        return 'data:image/png;base64,' + imagem_url
    except Exception as erro:
        raise Exception(f"Erro ao buscar serviços: {erro}")


def gerar_grafico_profissional_mais_procurado():
    """Gerar o gráfico de profissional mais procurado. Um gráfico de barras que 
    é alimentado pela contagem da coluna 'profissional' da planilha de
    profissionais. Esse gráfico é salvo em um buffer de memória e convertido
    para uma representação em base64, que é retornada para ser exibida na 
    página HTML.
    """
    try:
        if not os.path.exists(AGENDAMENTOS):
            return []
        
        df = pd.read_excel(AGENDAMENTOS, sheet_name="agendamentos")
        
        profissional_mais_procurado = df['profissional'].value_counts()
    
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.barplot(x=profissional_mais_procurado.index, y=profissional_mais_procurado.values, palette="viridis", ax=ax)
        ax.set_title('Profissional Mais Procurado')
        ax.set_xlabel('Profissionais')
        ax.set_ylabel('Quantidade')
        
        # Salvando imagem do gráfico no buffer de memória.
        imagem = io.BytesIO()
        fig.savefig(imagem, format="png")
        imagem.seek(0)

        # Criando uma representação ASCII para o HTML.
        imagem_url = base64.b64encode(imagem.getvalue()).decode()

        return 'data:image/png;base64,' + imagem_url
    except Exception as erro:
        raise Exception(f"Erro ao buscar serviços: {erro}")