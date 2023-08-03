# webcam_on_terminal
webcam_on_terminal is a little project that opens the webcam video on Linux's terminal. 

<p align="center">
  <img src="https://github.com/mathemaia/webcam_on_terminal/blob/main/data/demonstracao.gif">
</p>

# Dependencies installation
By default, the running of the program do the installation of all the libraries that are necessary to the execution of the main program. Although, if the user wants to do it manually, the commands bellow has to be executed first:

```
pip install numpy
pip install opencv-python
pip install tk
```

# Execution
There are two ways to execute the program, and both differs the result:

## * Running on window mode
Window mode will be executed if any parameter are passed. As the name says, the video will be showed in an window and not on terminal. The advantage of it is the stability of the execution, that will show all the frames with a clean interface.
```
python3 main.py
```

## * Running on terminal mode
On the other side of run it on window mode, the terminal mode may cause a bug on the the transition of the frames.
```
python3 main.py terminal
```
