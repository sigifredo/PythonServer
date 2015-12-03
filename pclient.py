#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, ssl, pprint

def client(text, ip = 'localhost', error=False):
    ret = True

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ss = ssl.wrap_socket(s, ca_certs="certs/server.crt", cert_reqs=ssl.CERT_REQUIRED)

        try:
            ss.connect((ip, 8888))
            ss.write('boo!')
            ss.close()
        except Exception, e1:
            if error:
                print e1
            ret = False
        finally:
            ss.close()
    except Exception, e2:
        if error:
            print e2
        ret = False

    return ret
