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

More information on this package can be found in the repository of this package: [printer-package](https://github.com/vives-projectweek-2022/autograder-printer-package/tree/master/printer_package)