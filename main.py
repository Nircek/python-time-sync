#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    python-time-sync

    Copyright (C) 2019 Nircek

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from socket import socket, AF_INET, SOCK_STREAM
from time import time

HOST = 'localhost'
PORT = 10001

with socket(AF_INET, SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.send(b'r')
    while sock.recv(1) != b'R':
        pass
    tx = time()
    sock.send(b'p')
    while sock.recv(1) != b'P':
        pass
    tz = time()
    sock.send(b't')
    while sock.recv(1) != b'T':
        pass
    ty = float(int.from_bytes(sock.recv(8), 'little'))
    ty += int.from_bytes(sock.recv(4), 'little')/10**9
    sock.send(b'c')
    while sock.recv(1) != b'C':
        pass
d = (tz-tx)/2
lty = tx+d;
delta = ty - lty;
print(f'tx = {tx}\nty = {ty}\ntz = {tz}\ndelta = {delta*1000} \N{PLUS-MINUS SIGN}{d*1000} ms')
