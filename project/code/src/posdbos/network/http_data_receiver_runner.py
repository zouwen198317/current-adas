#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 02.02.2017

:author: Paul Pasler
:organization: Reutlingen University
'''

import time
import sys, os
import logging
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from posdbos.network.http_data_receiver import HttpEEGDataReceiver

def run():
    hostname, port = ("localhost", 9000)
    client = HttpEEGDataReceiver(hostname, port, True)
    
    logging.info(client.getHeader())
    time.sleep(3)
    
    logging.info(client.getData())
    time.sleep(3)
    
    logging.info(client.getData())

if __name__ == "__main__":
    run()