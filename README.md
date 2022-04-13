# Dependencies

## OpenCV on Ubuntu / Linux

### Install OpenCV

```command
sudo apt update
sudo apt install libopencv-dev python3-opencv
```

### Verify OpenCV

```command
python3 -c "import cv2; print(cv2.__version__)"
```

(Version 4.2.0 at time of writing)
[source](https://linuxize.com/post/how-to-install-opencv-on-ubuntu-20-04/)

## Python

### Install Python & numpy

```command
sudo apt-get install python
sudo apt install numpy
```

### Verify Python

```command
python --version
```

[source](https://www.makeuseof.com/install-python-ubuntu/)

## openCV on windows/conda

### install anaconda 

[source](https://www.anaconda.com/products/individual)

#### select just me

![me](./img/anacondame.PNG)

##### chose a install location

![location](./img/anacondalocation.PNG)

#### register anaconda with python 

![setting](./img/anacondapython.PNG)

### install opencv and python

#### start anaconda with admin rights

![setting](./img/anacondaAdmin.png)

#### create environment

```bash
conda create — name opencv
activate opencv
```

#### install python , numpy & openCV

```bash
conda install python -y
conda install -c conda-forge opencv -y
conda install numpy -y
```

## Raspberry Pi

![pinout](./img/RPI-pinout.PNG)

[source](https://pi4j.com/1.4/pins/rpi-4b.html)

On the Pi, there is a Python file which will be the link between the Pi and the Nucleo (`print.py`).

A package has been made that can be installed by entering the following commands:

```bash
python3 -m pip install autograder-vives 
```

To use the package, run python (`python3`) and enter the following commands:

```bash
from printer import print
my_printer = Printer(port)
```

The 'my_printer' variable name can be changed to any variable name that you want to name your own printer instance. The port in the constructor has to be the correct port to which the Nucleo is connected to the Pi.
Now you can call the functions you want on the Printer object that has been created, or create more printer objects.

Details of the package can be found in this repository as well.

The Nucleo is connected to the Pi via the USB port for simplicity. The `print.py` file has 3 main functions, but can be expanded later to provide more functionality if needed.
First, it initiates an instance of the printer object. This is done by creating an object of the Printer class and specifying the connected port in the constructor. To check which USB port is in use:

```bash
dmesg | grep "tty"
```

Use the correct ACM port in the constructor (obtained from the command above).

Second, text can be printed. This is done simply by calling the 'print_text()' function on the Printer object, and entering a string as an argument in the function. This specified string will be printed. This is done by writing the string to the nucleo, which will read it and send that to the printer (further specifications on the printer library can be found on github). <!--- TO DO: put github link to printer repo--->

In this case, the data written to the Nucleo will be sent to the printer, and written back to the Pi (this gives a digital view of what has been printed, but this can be changed if desired).

Last, the port can also be changed, in case that would be necessary (e.g. in the event the USB connection is changed to another port on the Pi). This is done by calling the 'set_port' function on the Printer object, and passing the desired port as a string as an argument in the function. If you receive the text "Port updated to:" and the port you specified, then the change has been successful.
