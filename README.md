# Cheat de resposta automática do jogo BombParty com EasyOCR e PyAutoGUI 👀💻💣

Este projeto utiliza a biblioteca **EasyOCR** para reconhecer texto em imagens capturadas diretamente da tela e utiliza o **PyAutoGUI** para escrever automaticamente.

<br>

---

## 🔧 Funcionalidades

- 📸 **Captura de tela** em uma área específica.
- 🤖 **Reconhecimento de texto** com OCR (Reconhecimento Óptico de Caracteres).
- 🔍 **Sugestão automática** de palavras com base em um banco de palavras.
- ⌨️ **Entrada automatizada** de texto e envio.

<br>

---

## 📦 Ambiente virtual

_Não se esqueça de criar um ambiente virtual para não ter erros, segue passo a passo:_

 1. Vá até o caminho da sua pasta:
  - Caso estiver no próprio terminal da pasta não precisa fazer esse:
    ```bash
    cd caminho/da/sua/pasta
    ```
    
    <br>

2. Digite no terminal:
  - Caso use python:
    ```bash
    python -m venv .venv
    ```
  - Ou, caso use python3:
    ```bash
    python3 -m venv .venv
    ```

<br>

3. Agora ative o ambiente:
  - Windows:
    ```bash
    .venv\Scripts\activate
    ```
  - Linux ou Mac:
    ```bash
    source .venv/bin/activate
    ```

    <br>

---

## 🛠️ Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

```bash
pip install easyocr pillow pyautogui numpy
```

<br>

---

## 🔍 Verifique as coordenadas

No código, as coordenadas são fixas, ajuste-as de forma que a área delas sejam equivalentes à da bomba.
  - x1, y1, x2, y2
    ```bash
    coordenadas = (750, 560, 860, 610)
    ```

Caso precise ajustar as coordenadas, use o arquivo _**x_e_y.py**_, ao executar ele, criara uma janela com a posição X e Y do mouse, assim você conseguirá ajustar no código se for preciso

<br>

---

## 🛡️ Erros Comuns e Soluções


**_Erro: palavras.txt não encontrado_**

└── Verifique se o arquivo palavras.txt está na mesma pasta que o script.

<br>

**_Erro: imagem.png não encontrada_**

└── Certifique-se de que a imagem está na mesma pasta que o script.

<br>

**_Ele só começa a rodar o código quando o Pyautogui acha a imagem.png na tela, para evitar digitações desnecessárias_**

└── Troque a imagem para uma que simboliza que é a sua vez de jogar.

---

<br>

## ❌ Não me responsabilizo por nenhum banimento

- Eu não incentivo ninguém a usar esse Cheat

- Todas as partidas jogadas com ele foram feitas em salas privadas, com um ambiente controlado

- Esse é apenas um projeto para simular uma automação
