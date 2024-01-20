import unittest

from cases.export import TestExport
from cases.iterator import TestIterator
from cases.load_file import TestLoadFile
from cases.type_constructor import TestTypeConstructor
from cases.load_network import TestLoadNetwork
from cases.load_abbreviation import TestLoadAbbreviation

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestLoadFile("test_load_file_OSMWebsite"))
    suite.addTest(TestLoadFile("test_load_file_JOSM"))
    suite.addTest(TestLoadFile("test_load_file_level0"))
    suite.addTest(TestLoadAbbreviation("test_load_abbreviation"))
    suite.addTest(TestLoadNetwork("test_load_network_single_element"))
    suite.addTest(TestTypeConstructor("test_construct_elements"))
    suite.addTest(TestIterator("test_iterator_node"))
    suite.addTest(TestExport("test_self_save"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
