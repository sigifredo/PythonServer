#!/bin/env python
# -*- coding: utf-8 -*-

import socket, ssl, pprint

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ss = ssl.wrap_socket(s, ca_certs="certs/server.crt", cert_reqs=ssl.CERT_REQUIRED)

ss.connect(('localhost', 8888))

print ss.read()
ss.write('boo!')
print ss.read()
ss.close()
