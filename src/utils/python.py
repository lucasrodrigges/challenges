from subprocess import run
import os
from src.utils.starts_with import starts_with


def call_py_files(num):
    python_files = os.listdir('./src/py')

    for file_name in python_files:
        if starts_with(file_name, num):
            run(['python3', f'./src/py/{file_name}'])
            return

    print('File not found.')
