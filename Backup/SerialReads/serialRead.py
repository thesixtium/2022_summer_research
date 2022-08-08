import serial
import serial.rs485
import time
import struct
import sys
import glob
import serial.tools.list_ports

def serial_send(data_bytes, port, baud_rate, byte_size, parity, stop_bits):
    com_port = serial.Serial('COM' + str(port))  # open COM3
    com_port.baudrate = baud_rate
    com_port.bytesize = byte_size
    com_port.parity = parity
    com_port.stopbits = stop_bits
    com_port.rs485_mode = serial.rs485.RS485Settings()
    com_port.write(data_bytes)

    return_data = b''
    count = 0
    time.sleep(0.1)
    print(return_data)
    while return_data == b'' and count < 20:
        return_data = com_port.inWaiting()
        print(return_data)
        print(com_port.inWaiting())
        time.sleep(0.05)
    if count == 20:
        print("Timed out")
    return com_port.read(return_data)


# Vacuum Command Packet Structure
# Byte 0: Start Char
# Byte 1: Space
# Byte 2: Address
# Byte 3: Address
# Byte 4: Space
# Byte 5: Command
# Byte 6: Command
#       <- Data goes in here
# Byte 7: Space
# Byte 8: Checksum
# Byte 9: Checksum
# Byte 10: Terminator
def vacuum(value, port=3):
    baud_rate = 9600
    byte_size = 8
    parity = 'N'
    stop_bits = 1

    start_char = "~"
    address = 0x00
    terminator = "\r"

    if value == "time1":
        command = 0x72
        check_sum = address + command
        data = start_char + " " \
               + hex(address)[2:] + " " \
               + hex(command)[2:] + " " \
               + hex(check_sum)[2:] \
               + terminator
        data = serial_send(bytearray(data), port, baud_rate, byte_size, parity, stop_bits)
        data = data.decode("utf-8")
        if data[3:4] != "OK":
            print("Error occured")
        else:
            print(data[6:7])
    else:
        print("Invalid value")


def prevac_byte_assembly(data_length, function_code_msb, function_code_lsb, data):
    send_data = bytearray(b'\xBB')
    device_address = b'\xC8'
    host_address = b'\x00'

    crc = ((int.from_bytes(data_length, "big")
            + int.from_bytes(device_address, "big")
            + int.from_bytes(host_address, "big")
            + int.from_bytes(function_code_msb, "big")
            + int.from_bytes(function_code_lsb, "big")
            + int.from_bytes(data, "big")) % 256).to_bytes(1, byteorder='big')

    bytearray.append(send_data, int.from_bytes(data_length, "big"))
    bytearray.append(send_data, int.from_bytes(device_address, "big"))
    bytearray.append(send_data, int.from_bytes(host_address, "big"))
    bytearray.append(send_data, int.from_bytes(function_code_msb, "big"))
    bytearray.append(send_data, int.from_bytes(function_code_lsb, "big"))
    bytearray.append(send_data, int.from_bytes(data, "big"))
    bytearray.append(send_data, int.from_bytes(crc, "big"))

    print(send_data)

    return send_data


def prevac(value, port=3):
    baud_rate = 57600
    byte_size = 8
    parity = 'N'
    stop_bits = 1

    if value == "vacuum_value":
        data_length = b'\x01'
        function_code_msb = b'\x01'
        function_code_lsb = b'\x01'
        data = b'\x01'

        send_data = prevac_byte_assembly(data_length, function_code_msb, function_code_lsb, data)
        return_data = serial_send(send_data, port, baud_rate, byte_size, parity, stop_bits)[1:8]

        print(str(struct.unpack('d', return_data)[0]) + " mbar")

    elif value == "temp":
        data_length = b'\x00'
        function_code_msb = b'\x4C'
        function_code_lsb = b'\x06'
        data = b''

        send_data = prevac_byte_assembly(data_length, function_code_msb, function_code_lsb, data)
        print(send_data)
        return_data = serial_send(send_data, port, baud_rate, byte_size, parity, stop_bits)[1:8]

        print(str(return_data) + " K")

    elif value == "time":
        data_length = b'\x00'
        function_code_msb = b'\x4C'
        function_code_lsb = b'\x03'
        data = b''

        send_data = prevac_byte_assembly(data_length, function_code_msb, function_code_lsb, data)
        return_data = serial_send(send_data, port, baud_rate, byte_size, parity, stop_bits)[1:8]

        print(str(struct.unpack('l', return_data)[0]) + " sec")

    else:
        print("Invalid value")


def bcu14(value, port=3):
    if value == "temp":
        prevac(value, port)
    elif value == "time":
        prevac(value, port)
    else:
        print("Invalid value")


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def serial_ports_2():
    ports = serial.tools.list_ports.comports()

    for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))
