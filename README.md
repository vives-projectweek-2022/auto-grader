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

### Install Python

```command
sudo apt-get install python
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

![setting](./img/anacondaAdmin.PNG)

#### create environment

```bash
conda create — name opencv
activate opencv
```

#### install python & openCV

```bash
conda install python -y
conda install -c conda-forge opencv -y
```

## Raspberry Pi

![pinout](./img/RPI-pinout.PNG)
[source](https://pi4j.com/1.4/pins/rpi-4b.html)

## Thermal printer

Baud rate: 19200
[datasheet](https://cdn-shop.adafruit.com/datasheets/A2-user+manual.pdf)
![pinout](./img/printer-pinout.PNG)

import library: in empty repo (niet in git repo):

[source](https://os.mbed.com/components/Adafruit-Thermal-Printer/)

```commands
conda activate mbed
mbed import https://os.mbed.com/users/aross34/code/Thermal_HelloWorld/
```

thermal printer code file:

```commands
conda activate mbed
mbed new .
mbed toolchain GCC_ARM
mbed target NUCLEO_L476RG
mbed compile -f
```
