import serialRead

if __name__ == '__main__':
    serialRead.bcu14("temp", int(str(serialRead.serial_ports())[5]))