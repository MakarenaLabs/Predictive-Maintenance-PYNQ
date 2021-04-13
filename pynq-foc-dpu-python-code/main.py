from motor_controller import *
from motor_status_logger import *
from multiprocess_setting import *
from multiprocess_function import *
from DpuFocOverlay import *
from config import *
# from queue import Queue
from multiprocessing import Process, Queue

from pynq import allocate

from json import JSONEncoder

from flask import Flask, request, jsonify

app = Flask(__name__)


class JSON_Improved(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(JSON_Improved, self).default(obj)


app.json_encoder = JSON_Improved


@app.route('/rpm', methods=['POST'])
def set_rpm():
    rpm = int(request.json['rpm'])
    motor_controller.set_mode("rpm_mode")
    motor_controller.set_rpm(rpm)
    config["motor_control"]["ref"] = rpm
    return jsonify({'rpm': rpm})


@app.route('/torque', methods=['POST'])
def set_torque():
    ampere = int(request.json['torque'])
    motor_controller.set_mode("torque_mode")
    motor_controller.set_torque(ampere)
    config["motor_control"]["ref"] = ampere
    return jsonify({'torque': ampere})


@app.route('/reset', methods=['POST'])
def reset_motor():
    reset = int(request.json['reset'])
    if reset == 1:
        motor_controller.stop()
        return jsonify({'stop': 1})
    else:
        print("no reset")
        return jsonify({'stop': 0})


@app.route('/rpm', methods=['GET'])
def get_rpm():
    rpm = config["motor_control"]["ref"]
    return jsonify({'rpm': rpm})


@app.route('/logger', methods=['GET'])
def get_logger():
    motor_status.capture_mode(config["motor_logger"]["mode"])
    ret = logger_p.run()
    return jsonify(ret)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Loading Overlay")
    overlay = focDpuPL("../dpu.bit")
    #overlay.set_neural_network("/home/xilinx/jupyter_notebooks/pynq-dpu/dpu_resnet50.xmodel")

    print("Creating controller")
    motor_controller = Motor_Controller(overlay.get_xclbin())

    print("creating logger")
    motor_status = Motor_Status(overlay.get_xclbin())

    input_buffer = allocate(shape=(256,), dtype=np.uint8)
    capture_address = input_buffer.physical_address
    logger_p = logger(motor_status, capture_address)

    print(motor_status.mmio_blocks)

    app.run(host="0.0.0.0")
