import time
import numpy as np
from pynq import MMIO
from config import *
import threading
from queue import Queue


class controller(threading.Thread):
    def __init__(self, motor, control_mode="reset_mode", ref=None):
        threading.Thread.__init__(self)
        self._motor = motor
        self._motor.set_mode(control_mode)
        self._control_mode = control_mode
        self._ref = ref
        self._ref_value = 0

    def __del__(self):
        self._motor.stop()

    def run(self):
        while True:
            ref_value = self._ref.get()
            if (ref_value < -500 or ref_value > 500) and "rpm_mode" == self._control_mode:
                break
            if self._control_mode == "reset_mode":
                self._motor.stop()
            elif self._control_mode == "torque_mode":
                self._motor.set_torque(int(ref_value))
            elif self._control_mode == "rpm_mode":
                self._motor.set_rpm(int(ref_value))
                print(ref_value)
                print("")
            else:
                self._motor.stop()


class logger(object):
    def __init__(self, motor_status, capture_address):
        self._motor_status = motor_status
        self._capture_address = capture_address
        #self._mmio_stream = MMIO(capture_stream, 256)
        self._cap_list = [([]) for _ in range(4)]

    def run(self):
        mmio_stream = MMIO(self._capture_address, 256)
        self._motor_status.stream_capture(self._capture_address)
        for i in range(4, 260, 4):
            stream = mmio_stream.read(i - 4, 4)
            highbits, lowbits = divmod(stream, 0x10000)
            if i % 8 != 0:
                self._cap_list[0].extend([(np.int16(lowbits))])
                self._cap_list[1].extend([(np.int16(highbits))])
            else:
                self._cap_list[2].extend([(np.int16(lowbits))])
                self._cap_list[3].extend([(np.int16(highbits))])
        return self._cap_list

