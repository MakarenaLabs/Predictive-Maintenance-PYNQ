# Predictive-Maintenance-PYNQ

[MakarenaLabs s.r.l.](http://makarenalabs.com)

This repo is the open-source implementation for the Predictive Maintenance of Xilinx made with MakarenaLabs.
For more information about the other projects involved as dependencies please visit:
* [Vitis AI Github Repository](https://www.xilinx.com/products/design-tools/vitis/vitis-ai.html).
* [SPYN](https://github.com/Xilinx/IIoT-SPYN)
* [Electric Drive Demonstration Platform](https://github.com/Xilinx/IIoT-EDDP)
* [DPU-PYNQ](https://github.com/Xilinx/DPU-PYNQ)

# Setup
The project currently works with the [Motor Control Kit](https://shop.trenz-electronic.de/en/TEC0053-04-K1-EDDP-Motor-Control-Kit-with-Motor-Power-Supplies) provided by Trenz Electronic and supports the [Ultra96-V2](https://www.xilinx.com/products/boards-and-kits/1-vad4rl.html) board.
To connect to the power stage board of the motor is needed the [Adapter](https://shop.trenz-electronic.de/en/TEP0006-01-Ultra96-Pmod-Adapter) provided by Trenz Electronic.

# Instructions for Installation
To build the project you need to:
* Flash in a SD-Card the [Pynq image V2.6](http://www.pynq.io/board.html) for Ultra96-V2 from the ones available and follow the steps to setup the board.
* After having created a working PYNQ image, connect to the board and clone the repo.
* cd into the folder cloned and tap `chmod 755 init.sh && ./init.sh`. It will ask you the password, which is `xilinx` (same name as the account).
* Once the installation has completed you can try the Jupyter Notebooks provided as an example under `pynq-dpu` installed in the jupyter folder.

To run the flask server you need to tap `sudo python3 main.py` in the folder `pynq-foc-dpu-python-code`. 
Currently it is supported just the FOC interfacing.
The server will run in local (w.r.t. the Ultra96-V2) on the port 5000. For example, if your board has 192.168.2.5 IP address, the server is accessible through this address:
192.168.2.5:5000

Note that the python process is not detached, so you need to keep your SSH terminal active.

The documentation of Flask API server is here:
https://github.com/MakarenaLabs/Predictive-Maintenance-PYNQ/tree/main/pynq-foc-dpu-python-code

# Notes for Installation
The script `init.sh` will download and install the project [DPU-PYNQ](https://github.com/Xilinx/DPU-PYNQ) needed to interface the DPU.
