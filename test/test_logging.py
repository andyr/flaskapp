
import logging
import md5
import os
import random
import sys
import unittest

class TestLogging(unittest.TestCase):

    def setUp(self):
        self.filename = "/tmp/%s" % md5.new().hexdigest()[:5]
        self.logger = logging.getLogger(self.filename)

    def tearDown(self):
        # delete log file
        pass


if __name__ == '__main__':
    unittest.main()
