import easyocr
from PIL import ImageGrab
import numpy as np
import time
import pyautogui

reader = easyocr.Reader(['en']) 

def play(coordenadas):
    with open('palavras.txt', 'r', encoding='utf-8') as file:
        palavra = set(file.read().splitlines())
    
    usadas = set()
    while True:
        try:            
            if pyautogui.locateOnScreen('imagem.png', confidence=0.8):
                screenshot = np.array(ImageGrab.grab(bbox=coordenadas))
                resultado = reader.readtext(screenshot)
                if resultado:               
                    texto = " ".join(res[1] for res in resultado).strip()
                    texto = texto.upper().replace('l', 'I')
                    print(f"Texto identificado pelo OCR: {texto}")
                    
                    sugestoes = {p for p in palavras if texto in p.upper()} - usadas
                    if sugestoes:
                        palavra = sugestoes.pop()
                        pyautogui.write(palavra, interval=0.01)
                        pyautogui.press('enter')
                        usadas.add(palavra)
                time.sleep(0.8)
        except Exception as e:
            print(f"Erro: {e}")

coordenadas = (750, 560, 860, 610)
play(coordenadas)
