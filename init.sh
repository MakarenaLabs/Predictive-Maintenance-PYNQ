#!/bin/bash

echo "\n------INSTALL DPU-PYNQ ---------\n"
##############from DPU-PYNQ repo##################
git clone https://github.com/Xilinx/DPU-PYNQ.git
cd DPU-PYNQ/upgrade
sudo make

echo "\n------MAKE COMPLETE, PROCEEDING BUILD-------\n"
#install pynq-dpu
pip3 install pynq-dpu
cd $PYNQ_JUPYTER_NOTEBOOKS
pynq get-notebooks pynq-dpu -p .
###################################################

echo "\n------SUCCESSFULLY INSTALLED PYNQ-DPU------\n"
echo "\n------COPYING FOC EXAMPLE INTO JUPYTER HOME------\n"

#############setup FOC+DPU example#################
cp dpu-foc-predictive-maintenance.ipynb dpu_resnet50.xmodel $PYNQ_JUPYTER_NOTEBOOKS/pynq-dpu
###################################################

echo "\n------SUCCESS, NOW GO TO "
echo $PYNQ_JUPYTER_NOTEBOOKS
echo " TO RUN THE EXAMPLES, AND DON'T FORGET TO TRY THE LOCAL FLASK SERVER!\n"



