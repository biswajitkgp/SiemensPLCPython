import snap7
from snap7.util import get_bool

AREA_PE = 0x81  # Process Inputs

plc = snap7.client.Client()
plc.connect('192.168.1.105', 0, 1)

def read_inputs(byte_index=0, size=1):
    data = plc.read_area(AREA_PE, 0, byte_index, size)
    return [get_bool(data, 0, bit) for bit in range(8 * size)]

inputs = read_inputs()
print("Input states:", inputs)

plc.disconnect()
