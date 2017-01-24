#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 08.08.2016

:author: Paul Pasler
:organization: Reutlingen University
'''
from base_test import * # @UnusedWildImport

from util.eeg_data_source import EEGTablePacketSource, EEGTableWindowSource


class TestEEGTableToPacketConverter(BaseTest):

    def setUp(self):
        self.converter = EEGTablePacketSource(self.getData32CSV(), False)

    def test_convert_sunshine(self):
        self.assertFalse(self.converter.hasMore)
        self.converter.convert()
        self.assertTrue(self.converter.hasMore)
        for _ in range(0, len(self.converter.data)):
            self.converter.dequeue()
        self.assertFalse(self.converter.hasMore)

class TestEEGTableToWindowConverter(BaseTest):

    def setUp(self):
        self.converter = EEGTableWindowSource(self.getData1024CSV(), False, 1, 1)

    def test_convert_sunshine(self):
        self.assertFalse(self.converter.hasMore)
        self.converter.convert()
        self.assertTrue(self.converter.hasMore)
        for _ in range(0, len(self.converter.data)):
            self.converter.dequeue()
        self.assertFalse(self.converter.hasMore)


if __name__ == "__main__":
    unittest.main()