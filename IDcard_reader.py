#!/usr/bin/env python
# -*- coding: utf-8 -*-
import suica_select
import binascii
import nfc
import distance
import busio
import led
import time
clf = nfc.ContactlessFrontend('usb')
def main():
    while 1 :
        led.ld("1")
        if suica_select.start(clf)==1:
            continue
        time.sleep(0.5)
        led.ld("0")
        y=distance.main()
        return y
    clf.close()
if __name__ == '__main__':
    main()
