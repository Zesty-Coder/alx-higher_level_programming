#!/usr/bin/python3


a = True
if inherits_from(a, int):
    print("{} inherited class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited class {}".format(a, object.__name__))

