from pynq import allocate
from pynq import MMIO
from pynq_dpu import DpuOverlay
import time
import numpy as np

from utils import *


class Motor_Controller(object):  # TODO comments
    """Class for the motor control.
    This class is used to control the motor as well as read the status motor
    parameters. Motor control modes include: Speed mode and Current mode.
    In speed mode, the speed and direction of the motor are controlled using
    the RPM_Sp register. In current mode, the Torque_Sp register controls the
    current Iq to the motor. Relationship between current and torque is:
    Current = Torque*(0.00039)
    Attributes
    ----------
    mmio_blocks : dict
        A dict of IP blocks used by the motor controller.
    motor_modes : list
        A list of available modes of the motor controller.
    """

    def __init__(self, bitstream_path):
        self.registers = init_foc_on_platform(bitstream_path)  #
        self.mmio_control = MMIO(self.registers["foc_ctrl_reg"]["physical_address"],
                                 self.registers["foc_ctrl_reg"]["address_range"])  #
        self.mmio_blocks = {'control_axi_block': self.registers["foc_ctrl_reg"]["physical_address"]}
        self.motor_modes = ('reset_mode', 'torque_mode', 'rpm_mode')

    def set_mode(self, mode='reset_mode'):
        reg_list = ["CONTROL", "FLUX_SP", "FLUX_KP", "FLUX_KI", "TORQUE_SP", "TORQUE_KP",
                    "TORQUE_KI", "RPM_SP", "RPM_KP", "RPM_KI", "SHIFT", "VD", "VQ", "FA", "FB",
                    "CONTROL_REG2"]
        for reg in reg_list:
            if mode == 'torque_mode':
                self.mmio_control.write(self.registers["foc_ctrl_reg"]["control_registers"][reg]["offset"],
                                        self.registers["foc_ctrl_reg"]["control_registers"][reg][mode])
            elif mode == 'rpm_mode':
                self.mmio_control.write(self.registers["foc_ctrl_reg"]["control_registers"][reg]["offset"],
                                        self.registers["foc_ctrl_reg"]["control_registers"][reg][mode])
            else:
                self.mmio_control.write(self.registers["foc_ctrl_reg"]["control_registers"][reg]["offset"],
                                        self.registers["foc_ctrl_reg"]["control_registers"][reg][mode])

    def set_rpm(self, value):
        self.mmio_control.write(self.registers["foc_ctrl_reg"]["control_registers"]["RPM_SP"]["offset"], value)

    def set_torque(self, value):
        self.mmio_control.write(self.registers["foc_ctrl_reg"]["control_registers"]["TORQUE_SP"]["offset"], value)

    def stop(self):
        self.mmio_control.write(self.registers["foc_ctrl_reg"]["control_registers"]["CONTROL"]["offset"],
                                self.registers["foc_ctrl_reg"]["control_registers"]["CONTROL"]["reset_mode"])

    def _read_controlreg(self, value):
        return self.mmio_control.read(value)

    def _write_controlreg(self, offset, value):
        self.mmio_control.write(offset, value)

