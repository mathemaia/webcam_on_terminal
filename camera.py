import subprocess


# VIRTUAL ENVIROMENT
###################################################################################################
subprocess.check_call(['pip', 'install', 'numpy'])
subprocess.check_call(['pip', 'install', 'opencv-python'])
subprocess.check_call(['pip', 'install', 'tk'])

import numpy as np
import cv2
import tkinter as tk
###################################################################################################



# IMAGE CONVERSOR
###################################################################################################
def convert_image(image, size):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (round(image.shape[1] * (1/size)), round(image.shape[0] * (1/size))))

    new_image = np.zeros((image.shape[0], image.shape[1])).astype(int).astype(str)

    # .
    min = 0
    max = 25
    mask = (image >= min) & (image <= max)
    new_image[mask] = ' '

    # -
    min = 25
    max = 50
    mask = (image > min) & (image <= max)
    new_image[mask] = '.'

    # "
    min = 50
    max = 75
    mask = (image > min) & (image <= max)
    new_image[mask] = '+'

    # *
    min = 75
    max = 100
    mask = (image > min) & (image <= max)
    new_image[mask] = ':'

    # !
    min = 100
    max = 125
    mask = (image > min) & (image <= max)
    new_image[mask] = '*'

    # ?
    min = 125
    max = 150
    mask = (image > min) & (image <= max)
    new_image[mask] = '='

    # 1
    min = 150
    max = 175
    mask = (image > min) & (image <= max)
    new_image[mask] = '4'

    # &
    min = 175
    max = 200
    mask = (image > min) & (image <= max)
    new_image[mask] = '0'

    # 0
    min = 200
    max = 225
    mask = (image > min) & (image <= max)
    new_image[mask] = '&'

    # @
    min = 225
    max = 250
    mask = (image > min) & (image <= max)
    new_image[mask] = '@'

    # Imprimir a matriz formatada com colunas alinhadas
    return new_image 
###################################################################################################



# WEBCAM TRANSFORMATION
###################################################################################################
# Função para formatar a matriz como uma string de matriz
def format_matrix(matrix):
    return '\n'.join([' '.join(row) for row in matrix])

# Captura da câmera
cap = cv2.VideoCapture(0)

length = 5

# Verificar se a câmera foi aberta corretamente
if not cap.isOpened():
    print("Erro ao abrir a câmera.")
    cap.release()
    exit()

# Criar a janela do tkinter
root = tk.Tk()
root.title("Vídeo ASCII")
root.configure(bg="black")  # Definir o background para preto

# Criar um rótulo para exibir as matrizes na janela com fonte menor
label = tk.Label(root, text="", font=("Courier New", 10), bg="black", fg="#777777")
label.pack()

# Função para capturar cada frame da câmera e atualizar o rótulo com a matriz convertida em ASCII
def update_frame():
    while True:
        ret, frame = cap.read()

        if not ret:  # Verifica se a captura falhou ou o vídeo acabou
            break
        frame = convert_image(frame, length)
        formatted_matrix = format_matrix(frame)

        try:
            if root.winfo_exists():  # Verifica se a janela ainda está aberta
                label.config(text=formatted_matrix)
                root.update()
        except tk.TclError:
            break

# Chamar a função para exibir o vídeo da câmera em ASCII
update_frame()

cap.release()  # Liberar a captura da câmera após fechar a janela

root.mainloop()
###################################################################################################