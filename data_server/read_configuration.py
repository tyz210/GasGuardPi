import json
import os.path

PORT = None

root_dir = os.path.dirname(__file__) or '.'

with open('{}/configuration.json'.format(root_dir)) as data_file:
    data = json.load(data_file)
    PORT = data['namespace']
