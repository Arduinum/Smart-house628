conf_port_arduino = {'port': '/dev/ttyACM0', 'speed': 9600, 'timeout': 1}


def get_conf_port(key):
    return conf_port_arduino[key]
