#!/usr/bin/env python
# -*- coding: utf-8 -*-

import signal
import socket
import sys
import ssl
import time
from thread import *

HOST = ''
PORT = 8888

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='certs/server.crt', keyfile='certs/server.key')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket creado'

def signalHandler(signal, frame):
    print 'Cerrando conexión'
    s.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signalHandler)
signal.signal(signal.SIGTERM, signalHandler)

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error code',str(msg[0]),' Mensaje: ',msg[1]
    sys.exit(1)

print 'Socket bind complete'

s.listen(10)

print 'Socket now listening'

def clientthread(conn, addr):
    f = open(addr[0] + '-' + str(addr[1]) + '.txt', 'ab')
    f.write('# ' + time.strftime('%d-%m-%Y %H:%M:%S') + '\n')
    # conn.send('todo bien')

    while True:
        data = conn.recv(1024)
        f.write(data)
        # reply = 'Recibido: ' + data
        if not data:
            break
        # conn.sendall(reply)

    print 'Conexión terminada con ' + addr[0]
    f.close()
    conn.close()

while True:
    try:
        conn, addr = s.accept()
        print 'Estableciendo conexión con ' + addr[0] + ': ' + str(addr[1])
        connstream = context.wrap_socket(conn, server_side=True)
        print 'Conectado con ' + addr[0] + ': ' + str(addr[1])
        start_new_thread(clientthread, (connstream, addr))
    except Exception, ex:
        print 'Error (' + str(ex[0]) + '): ' + ex[1]

s.close()
