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

## openCV on windows/WSL

### install VcXsrv Server

[source](https://sourceforge.net/projects/vcxsrv/)

### configure VcXsrv server

![windows](./img/xming_win_conf.PNG)

![setting](./img/xming_extra.PNG)

### WSL

```command
sudo apt-get install x11-apps

DISPLAY=<IP van pc>:0.0 xhost <IP van pc>

python3 test.py && xeyes
```

## Raspberry Pi

![pinout](./img/RPI-pinout.PNG)
[source](https://pi4j.com/1.4/pins/rpi-4b.html)
Check which USB port is in use:

```bash
dmesg | grep "tty"
```

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
