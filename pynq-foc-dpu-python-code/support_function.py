import time
import numpy as np
from pynq import MMIO
from config import *

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

