#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import serial
import json
from json.decoder import JSONDecodeError
import sys
import os.path
import time

SERIAL_PORT = 9600

# TODO: Add device detection
serial = serial.Serial('/dev/cu.usbmodemFA131', SERIAL_PORT)

PORT_NUMBER = None

ROOT_DIR = os.path.dirname(__file__) or '.'


def publish_data(data):
    # TODO: Add more output sources
    print(json.loads(data))


def main():
    CONFIG = None
    with open('{}/configuration.json'.format(ROOT_DIR)) as data_file:
        CONFIG = json.load(data_file)

    serial.close()
    serial.open()
    try:
        while True:
            if CONFIG:
                time.sleep(CONFIG['read_time'])

            data = serial.readline().decode("utf-8")
            publish_data(data)

    except KeyboardInterrupt:
        print('\nClose read session.')
    except JSONDecodeError:
        print('\nIncorrect data structure.')
    except:
        print('\nProblem: {}'.format(sys.exc_info()[0]))
    finally:
        serial.close()


if __name__ == "__main__":
    main()
