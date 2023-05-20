from sys import argv
from src.utils.javascript import call_js_files
from src.utils.python import call_py_files

if len(argv) != 3:
    print("How to use: python3 run.py <language> <test_number>")
else:
    language = argv[1]

    if language == 'js':
        call_js_files(argv[2])
    if language == 'py':
        call_py_files(argv[2])
