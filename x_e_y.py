import tkinter as tk
import pyautogui

def update_mouse_position():
    # Obtém a posição atual do mouse
    x, y = pyautogui.position()
    
    # Atualiza o texto na label com a posição atual do mouse
    position_label.config(text=f"Posição do mouse: X = {x}, Y = {y}")
    
    # Chama esta função novamente após 100ms
    window.after(100, update_mouse_position)

# Cria a janela principal usando Tkinter
window = tk.Tk()
window.title("Posição do Mouse em Tempo Real")

# Cria um label para exibir a posição do mouse
position_label = tk.Label(window, text="Posição do mouse: X = 0, Y = 0", font=("Helvetica", 16))
position_label.pack(pady=20)

# Chama a função pela primeira vez para iniciar o loop de atualização
update_mouse_position()

# Inicia o loop da interface gráfica
window.mainloop()
