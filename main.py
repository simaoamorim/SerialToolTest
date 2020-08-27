import serial


if __name__ == '__main__':
    try:
        ser = serial.Serial(
            port='/dev/ttyUSB0',
            baudrate=19200,
            bytesize=serial.SEVENBITS,
            parity=serial.PARITY_EVEN,
            stopbits=serial.STOPBITS_TWO,
            rtscts=False,
            xonxoff=True,
            dsrdtr=False
        )
        if ser.is_open:
            with open('script.nc', 'r') as script:
                content = script.read()
                content_bytes = content.encode('UTF-8')
                ser.write(content_bytes)
            print('Done')
    except serial.SerialException as e:
        print(e)
        exit(-1)
