#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pclient

print pclient.client('texto')
print pclient.client('texto', error=True)
# print pclient.client('texto', 'localhost', True)
