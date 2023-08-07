# webcam_on_terminal
This little project intends to open the your webcam in Linux's terminal.

<p align="center">
  <img src="https://github.com/mathemaia/webcam_on_terminal/blob/main/data/demo.gif">
</p>

# Dependencies installation
By default, the running of the program do the installation of all the necessary libraries to the execution. Although, if the user wants to do it manually, the commands bellow has to be executed first and in this :

```
pip install numpy
pip install opencv-python
pip install tk
```

# Execution:
There are two ways to execute the program, and both differs the results:

- ## Running on window mode
Window mode will be executed if any parameter are passed. As the title, the video will be showed in an window and not on terminal. The advantage of it is the stability of the execution, that will show all the frames with a clean interface and with any bug.
```
python3 main.py
```

- ## Running on terminal mode
On the other hand, the terminal mode may cause a bug on the the transition of the frames because each frame has to be printed as a string. Until I fix this issue the program will run on window mode when any argument be passed.
```
python3 main.py terminal
```

# How does it work?
OpenCV was used to access and get the frames of webcam. Each frame is passed to a function that does a transformation in the matrix frame. The image bellow shows the steps of this process.

<p align="center">
  <img src="https://github.com/mathemaia/webcam_on_terminal/blob/main/data/all.png">
</p>
