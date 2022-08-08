# bb 01 c8 01 01 01 01 cd

import serial


class SerialDevice:
    def __init__(self, port_name='COM4', baudrate=57600, timeout=10):
        self.port = serial.Serial()
        self.port.port = port_name
        self.port.baudrate = baudrate
        self.port.timeout = timeout

    def open(self, port_name=None, baudrate=None, timeout=None):
        if port_name is not None:
            self.port.port = port_name
        if baudrate is not None:
            self.port.baudrate = baudrate
        if timeout is not None:
            self.port.timeout = timeout

        self.close()

        self.port.open()
        if not self.port.is_open:
            raise IOError(f'Open failed on port {self.port.port}')

    def close(self):
        if self.port.is_open:
            self.port.close()

    def send_cmd(self, command):
        """Send command and read reply"""
        if not self.port.is_open:
            raise IOError('Port is not open')
        self.port.write(f'{command}\r'.encode())
        reply = self.port.read_until(b'\r')  # My device uses /r as a terminator
        if not reply:
            raise IOError('Read timeout error')
        return reply.decode()


ser = SerialDevice()
ser.open()
ser.send_cmd("bb 01 c8 01 01 01 01 cd")
ser.close()
