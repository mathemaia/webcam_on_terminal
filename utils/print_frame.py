import numpy as np
import sys

def print_frame(frame):
    # Sequência de escape ANSI para limpar a tela
    print("\033[2J", end='')

    np.savetxt(sys.stdout, frame, delimiter='', fmt='%2s')

    # Sequência de escape ANSI para posicionar o cursor no início da tela
    print("\033[H", end='')