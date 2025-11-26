import os
import time
from flask import Flask, render_template
import webbrowser
from threading import Thread

from .graphics import (gerar_grafico_servico_mais_procurado, 
                      gerar_grafico_profissional_mais_procurado)


# Cria um aplicativo simple Flask.
app = Flask(__name__)


@app.route("/")
def plotar_graficos():
    """Define a única rota; por meio dessa rota a imagem em formato base64 é 
    passada ao renderizador de HTML flask, que por sua vez encaminha a imagem 
    para uma variável no HTML.
    """
    img1_url = gerar_grafico_profissional_mais_procurado()
    img2_url = gerar_grafico_servico_mais_procurado()
    
    return render_template("index.html", img1_url=img1_url, img2_url=img2_url)


def abrir_navegador():
    """Inicia o servidor Flask em background e abre o navegador."""
    # inicia o servidor numa thread separada
    time.sleep(2)  # espera o servidor iniciar
    webbrowser.open_new('http://127.0.0.1:5000')
    
    
def executar_servidor():
    Thread(target=abrir_navegador).start()
    app.run(debug=True, use_reloader=False)
