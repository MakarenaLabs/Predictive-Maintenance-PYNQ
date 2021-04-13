from pynq_dpu import DpuOverlay


class focDpuPL(object):
    def __init__(self, xclbin_path: str):
        self._xclbin = DpuOverlay(xclbin_path)

    def set_neural_network(self, xmodel_path: str):
        self._xclbin.load_model(xmodel_path)
        return

    def get_xclbin(self):
        return self._xclbin

    def get_ip_map(self):
        return self._xclbin.ip_dict
