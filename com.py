import serial



#handshake = [b'0x26', b'0x30', b'0x30', b'0x30', b'0x38', b'0x30', b'0x2A']
handshake = b'\x26\x30\x30\x30\x38\x30\x2A'
record=b'\x23\x37\x31\x30\x30\x2A'


def main():



    with serial.Serial(parity = serial.PARITY_EVEN) as ser:
        ser.baudrade = 9600
        ser.port = '/dev/ttyUSB0'
        ser.stopbits = 1
        # ser.partiy = serial.PARITY_EVEN
        ser.open()
        ser.flush()
        print(ser, end="\n\n")
        
        read = ser.read(5)
        print(read)

        ser.write(handshake)
        print(f'sent {handshake}')

        import time
        time.sleep(5)
        print("awake")

        ser.write(record)
        print(f"sent {[hex(x) for x in record]}")

        while True:
            print(hex(ser.read(1)[0]))


if __name__ == "__main__":
    main()