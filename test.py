#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pclient

print pclient.send2server('texto')
print pclient.send2server('texto', error=True)
print pclient.send2server('texto', 'localhost', True)
print pclient.send2servers('texto', ['localhost', '127.0.0.1'])
print pclient.send2servers('texto', ['localhost', '127.0.0.1'], True)
