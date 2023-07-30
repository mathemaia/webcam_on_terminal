import numpy as np
import sys

def print_frame(frame):
    '''Print the frame on terminal and reposition it on the same place to give the impression of movemant'''
    
    # ANSI scape sequence to clean the terminal
    print("\033[2J", end='')

    # print the frame on terminal
    np.savetxt(sys.stdout, frame, delimiter='', fmt='%2s')

    # ANSI scape sequence to put the cursor on the beggining oh terminal
    print("\033[H", end='')