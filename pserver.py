#!/bin/env python
# -*- coding: utf-8 -*-

import signal
import socket
import sys
import ssl
from thread import *

HOST = ''
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket creado'
ss = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1, ciphers="ADH-AES256-SHA")
print 'Socket asegurado'

def signalHandler(signal, frame):
    print 'Cerrando conexión'
    ss.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signalHandler)
signal.signal(signal.SIGTERM, signalHandler)

try:
    ss.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error code',str(msg[0]),' Mensaje: ',msg[1]
    sys.exit(1)

print 'Socket bind complete'

ss.listen(10)

print 'Socket now listening'

def clientthread(conn):
    conn.send('todo bien')

    while True:
        data = conn.recv(1024)
        reply = 'Recibido: ' + data
        if not data:
            break
        conn.sendall(reply)

    conn.close()

while 1:
    conn, addr = ss.accept()
    print 'Conectado con ' + addr[0] + ': ' + str(addr[1])
    start_new_thread(clientthread, (conn,))

ss.close()
