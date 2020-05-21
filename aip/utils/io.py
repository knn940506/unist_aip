import requests
import os

def read_file(path):
    with open(path, 'r') as fp:
        res = fp.read()
    return res

def write_file(dir, file_name, text):
    if not file_name.endswith('pddl'):
        file_name += '.pddl'

    with open(os.path.join(dir, file_name), 'w') as fp:
        fp.write(text)

def write_file_from_url(dir, file_name, url):
    text = requests.get(url).text
    write_file(dir, file_name, text)