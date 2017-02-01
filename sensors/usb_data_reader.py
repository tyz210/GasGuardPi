#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import serial

SERIAL_PORT = 9600

# TODO: Add device detection
ser = serial.Serial('/dev/cu.usbmodemFD121', SERIAL_PORT)


def publish_data(data):
    # TODO: Add more output sources
    print(data)


def main():
    ser.close()
    ser.open()
    try:
        while True:
            # TODO: Add timer for data reading
            publish_data(data=ser.readline())
    except:
        ser.close()
        print('\nClose read session.')


if __name__ == "__main__":
    main()
