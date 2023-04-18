import unittest

from test_export import TestExport
from test_iterator import TestIterator
from test_load_file import TestLoadFile

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestLoadFile("test_load_file_OSMWebsite"))
    suite.addTest(TestLoadFile("test_load_file_JOSM"))
    suite.addTest(TestLoadFile("test_load_file_level0"))
    suite.addTest(TestIterator("test_iterator_node"))
    suite.addTest(TestExport("test_self_save"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
