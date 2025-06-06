# Import snap7 driver for communication between python with PLC S7-1200
import snap7
from snap7.util import *

def write_bool_array_to_plc(plc_ip, db_number, start_byte, bool_array):
    plc = snap7.client.Client()
    try:
        plc.connect(plc_ip, rack=0, slot=1)  # This is the default PLC S7-1200 hardware configuration
        
        if plc.get_connected():
            print(f"Connected to PLC at {plc_ip}")
            num_bytes = (len(bool_array) + 7) // 8  # Normally one byte=8bits ex: QB0 (Q0.0, Q0.1....Q0.7)
            data = plc.db_read(db_number, start_byte, num_bytes)
            for i, value in enumerate(bool_array):
                byte_index = i // 8  # Byte index
                bit_index = i % 8   # Bit index with the byte
                set_bool(data, byte_index, bit_index, value)
            plc.db_write(db_number, start_byte, data)
            print(f"Write arrays to TIA Portal are DB{db_number} starting at byte {start_byte}")
        else:
            print("Fault connected to PLC S7-1200")
    finally:
        plc.disconnect()



plc_ip = '192.168.1.105' # PLC IP address configured on TIA Portal V19
db_number = 1  # Connect to data block number 1 of TIA Portal V19
start_byte = 0  # Starxt byte in data block
#bool_array = [True, True, True, True]
#bool_array = [False, False, False, False]
bool_array = [True, False, False, True]

write_bool_array_to_plc(plc_ip, db_number, start_byte, bool_array)