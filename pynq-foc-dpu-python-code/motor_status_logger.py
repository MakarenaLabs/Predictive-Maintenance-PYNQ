from pynq import allocate
from pynq import MMIO
from pynq_dpu import DpuOverlay
import time
import numpy as np

from utils import *


class Motor_Status(object):  # TODO comments
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
        self.mmio_capture = MMIO(self.registers["capture_stream_data"]["physical_address"],
                                 self.registers["capture_stream_data"]["address_range"])  #
        self.mmio_blocks = {'capture_axi_block': hex(self.registers["capture_stream_data"]["physical_address"])}
        self.motor_capture_modes = ('ia_ib_angle_rpm', 'id_iq', 'vd_vq')

    def capture_mode(self, mode='ia_ib_angle_rpm'):
        reg = "CONTROL_REG2"
        if mode == 'ia_ib_angle_rpm':
            self.mmio_control.write(self.registers["foc_ctrl_reg"]["control_registers"][reg]["offset"],
                                    self.registers["capture_stream_data"]["modes"]["CAPTURE_IA_IB_ANGLE_RPM"])
        elif mode == 'id_iq':
            self.mmio_control.write(self.registers["foc_ctrl_reg"]["control_registers"][reg]["offset"],
                                    self.registers["capture_stream_data"]["modes"]["CAPTURE_ID_IQ"])
        elif mode == 'vd_vq':
            self.mmio_control.write(self.registers["foc_ctrl_reg"]["control_registers"][reg]["offset"],
                                    self.registers["capture_stream_data"]["modes"]["CAPTURE_VD_VQ"])
        else:
            self.mmio_control.write(self.registers["foc_ctrl_reg"]["control_registers"][reg]["offset"],
                                    self.registers["capture_stream_data"]["modes"]["CAPTURE_IA_IB_ANGLE_RPM"])

    def _read_controlreg(self, value):
        return self.mmio_control.read(value)

    def _write_controlreg(self, offset, value):
        self.mmio_control.write(offset, value)

    def write_capturereg(self, offset, value):
        self.mmio_capture.write(offset, value)

    def read_capturereg(self, offset):
        return self.mmio_capture.read(offset)

    def stream_capture(self, capture_address):
        # Offset 0 - Control reg
        self.write_capturereg(0x00, 0)
        # Offset 4 - Transfer size
        self.write_capturereg(0x04, 256)
        print(f'Transfer count: {self.read_capturereg(0x08)}')
        # Offset 12 - Start address
        self.write_capturereg(0x0C, capture_address)
        # Offset 16 - End address
        #self.write_capturereg(0x14, capture_address + 256)
        # Offset 0 - Control reg
        self.write_capturereg(0x00, 0)
        self.write_capturereg(0x00, 2)
        self.write_capturereg(0x00, 3)
        self.write_capturereg(0x00, 0)
        # Offset 8 - Transfer count
        # print(f'Transfer count: {motor.read_capturereg(8)}')