#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 30.05.2016

:author: Paul Pasler
:organization: Reutlingen University
'''
import os
import threading

from config.config import ConfigProvider
from posdbos import PoSDBoS


scriptPath = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__': # pragma: no cover
    experiments = ConfigProvider().getExperimentConfig()
    experimentDir = experiments["filePath"]
    #filePath = "%s/test/%s" % (experimentDir, "awake_full.csv")
    filePath = "%s/test/%s" % (experimentDir, "drowsy_full.csv")

    p = PoSDBoS("knn_1", True, filePath)
    print "START"
    pt = threading.Thread(target=p.run)
    pt.start()

    pt.join()
    print "END"