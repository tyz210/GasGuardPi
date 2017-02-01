#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os.path

PORT_NUMBER = None

root_dir = os.path.dirname(__file__) or '.'

with open('{}/configuration.json'.format(root_dir)) as data_file:
    data = json.load(data_file)
    PORT_NUMBER = data['port_number']
