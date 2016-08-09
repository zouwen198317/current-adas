#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 02.08.2016

:author: Paul Pasler
:organization: Reutlingen University
'''
from util.quality_util import QualityUtil
from util.signal_util import SignalUtil
from numpy import NaN
from config.config import ConfigProvider
from util.eeg_util import EEGUtil

class SignalProcessor(object):
    def __init__(self, verbose=False):
        self.maxNaNValues = ConfigProvider().getProcessingConfig().get("maxNaNValues")
        self.qualUtil = QualityUtil()
        self.sigUtil = SignalUtil()
        self.verbose = verbose

    def process(self, raw, quality):
        raw = self._replaceBadQuality(raw, quality)
        raw = self._replaceSequences(raw)
        raw = self._replaceOutliners(raw)
        raw = self._normalize(raw)
        invalid = self.qualUtil.isInvalidData(raw)
        return raw, invalid

    def _replaceBadQuality(self, raw, quality):
        if self.verbose:
            print "badQuality: %d" % self.qualUtil.countBadQuality(raw, quality)
        raw = self.qualUtil.replaceBadQuality(raw, quality, NaN)
        self._printNaNCount(raw)
        return raw

    def _replaceSequences(self, raw):
        if self.verbose:
            print "sequences: %d" % self.qualUtil.countSequences(raw)
        raw = self.qualUtil.replaceSequences(raw)
        self._printNaNCount(raw)
        return raw

    def _replaceOutliners(self, raw):
        if self.verbose:
            print "outliners: %d" % self.qualUtil.countOutliners(raw)
        raw = self.qualUtil.replaceOutliners(raw, NaN)
        self._printNaNCount(raw)
        return raw

    def _normalize(self, raw):
        if self.verbose:
            print "normalize: min %.2f max %.2f" % (self.sigUtil.minimum(raw),self.sigUtil.maximum(raw)) 
        raw = self.sigUtil.normalize(raw)
        if self.verbose:
            print "normalize: min %.2f max %.2f" % (self.sigUtil.minimum(raw),self.sigUtil.maximum(raw)) 
        self._printNaNCount(raw)
        return raw

    def _printNaNCount(self, raw):
        if self.verbose:
            print "NaN count: %s" % self.qualUtil.countNans(raw)

class EEGProcessor(object):
    def __init__(self, verbose=False):
        self.samplingRate = ConfigProvider().getEmotivConfig().get("samplingRate")
        self.qualUtil = QualityUtil()
        self.eegUtil = EEGUtil()
        self.verbose = verbose

    def process(self, proc):
        return self.eegUtil.getAlphaWaves(proc, self.samplingRate)