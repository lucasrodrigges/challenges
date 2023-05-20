from subprocess import run
import os
from src.utils.starts_with import starts_with


def call_js_files(num):
    js_files = os.listdir('./src/js')

    for file_name in js_files:
        if starts_with(file_name, num):
            run(['node', f'./src/js/{file_name}'])
            return

    print('File not found.')
