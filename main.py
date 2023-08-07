from utils.image_conversor import convert_image
from utils.matrix_formatation import format_matrix
from utils.print_frame import print_frame
import subprocess
import sys


# import or install Numpy
try:
	__import__('numpy')
except:
    subprocess.check_call(['pip', 'install', 'numpy'])

# import or install OpenCV
try:
    __import__('cv2')
except:
    subprocess.check_call(['pip', 'install', 'opencv-python'])
import cv2

# import or install Tkinter
try:
    __import__('tk')
except:
    subprocess.check_call(['pip', 'install', 'tk'])
import tkinter as tk


### MAIN
if __name__ == '__main__':
    # access the camera
    cap = cv2.VideoCapture(0)

    # if the argument passed, it will run on terminal
    if len(sys.argv) == 2:
        if sys.argv[1] == 'terminal':
            while True:
                ret, frame = cap.read()
                print_frame(convert_image(frame, 9))
        else:
            print('Invalid argument.')

    # if any argument is passed, run on window
    else:
        # create the window
        root = tk.Tk()
        root.title("Vídeo ASCII")
        root.configure(bg="black")  

        # create a label to show the matrix of the frame
        label = tk.Label(root, text="", font=("Courier New", 10), bg="black", fg="#CDCBC4")
        label.pack()

        # verify the camera's integrity
        if not cap.isOpened():
            print("Erro ao abrir a câmera.")
            cap.release()
            exit()
        
        # take the webcam's frame and do the transformation
        while True:
            ret, frame = cap.read()

            if not ret:  
                break
            frame = convert_image(frame, 5)
            formatted_matrix = format_matrix(frame)

            try:
                if root.winfo_exists():
                    label.config(text=formatted_matrix)
                    root.update()
            except tk.TclError:
                break
            
        cap.release()
        root.mainloop()
