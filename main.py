import easyocr  # Biblioteca para reconhecimento de texto em imagens (OCR)
from PIL import ImageGrab  # Permite capturar capturas de tela
import numpy as np  # Biblioteca para manipulação de arrays numéricos
import time  # Para gerenciar atrasos e intervalos no código
import pyautogui  # Para automação de interações com a interface gráfica

# Inicializa o leitor 
reader = easyocr.Reader(['pt']) 

# Função principal
def play(coordenadas):
    # Configurar o arquivo palavras.txt
    with open('palavras.txt', 'r', encoding='utf-8') as file:
        palavra = set(file.read().splitlines())
    
    usadas = set()  # Conjunto para armazenar palavras já sugeridas
    while True:  # Loop infinito para reconhecimento contínuo
        try:
            # Verifica se a imagem 'imagem.png' está presente na tela (confiança de 80%)
            if pyautogui.locateOnScreen('imagem.png', confidence=0.8):
                # Captura a região especificada da tela e converte para um array NumPy
                screenshot = np.array(ImageGrab.grab(bbox=coordenadas))
                # Aplica OCR na captura da tela
                resultado = reader.readtext(screenshot)
                if resultado:  # Se o OCR identificar algum texto na captura
                    # Combina os textos reconhecidos em uma única string
                    texto = " ".join(res[1] for res in resultado).strip()
                    # Converte o texto para maiúsculas e substitui 'l' por 'I' (para corrigir confusão visual)
                    texto = texto.upper().replace('l', 'I')
                    print(f"Texto identificado pelo OCR: {texto}")
                    
                    # Filtra as palavras carregadas para encontrar aquelas que contêm o texto reconhecido
                    sugestoes = {p for p in palavras if texto in p.upper()} - usadas
                    if sugestoes:  # Se houver sugestões disponíveis
                        # Remove e obtém uma palavra das sugestões
                        palavra = sugestoes.pop()
                        # Escreve a palavra na tela com um intervalo de 10ms entre os caracteres
                        pyautogui.write(palavra, interval=0.01)
                        # Pressiona a tecla Enter após digitar a palavra
                        pyautogui.press('enter')
                        # Adiciona a palavra ao conjunto de palavras já usadas
                        usadas.add(palavra)
                # Aguarda 0.4 segundos antes de capturar novamente (para evitar mandar alguma mensagem no chat do jogo)
                time.sleep(0.4)
        except Exception as e:  # Captura e exibe qualquer erro que possa ocorrer
            print(f"Erro: {e}")

# Coordenadas da região da tela onde o texto será capturado (x1, y1, x2, y2)
coordenadas = (750, 560, 860, 610)

# Inicia o reconhecimento de texto na tela com as coordenadas especificadas
play(coordenadas)
