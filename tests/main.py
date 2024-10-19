import unittest

from cases.core.export import TestExport
from cases.core.iterator import TestIterator
from cases.core.load_abbreviation import TestLoadAbbreviation
from cases.core.load_file import TestLoadFile
from cases.core.load_network import TestLoadNetwork
from cases.plugin.plugin_driver_poly import TestPluginDriverPoly
from cases.core.type_constructor import TestTypeConstructor

if __name__ == "__main__":
    suite = unittest.TestSuite()
    # TestExport
    suite.addTest(TestExport("test_self_save"))
    # TestIterator
    suite.addTest(TestIterator("test_iterator_node"))
    # TestLoadAbbreviation
    suite.addTest(TestLoadAbbreviation("test_load_abbreviation"))
    # TestLoadFile
    suite.addTest(TestLoadFile("test_load_file_OSMWebsite"))
    suite.addTest(TestLoadFile("test_load_file_JOSM"))
    suite.addTest(TestLoadFile("test_load_file_level0"))
    # TestLoadNetwork
    suite.addTest(TestLoadNetwork("test_load_network_single_element"))
    # TestPluginDriverPoly
    suite.addTest(TestPluginDriverPoly("test_plugin_driver_poly_import"))
    suite.addTest(TestPluginDriverPoly("test_plugin_driver_poly_cli"))
    # TestTypeConstructor
    suite.addTest(TestTypeConstructor("test_construct_elements"))
    # Run
    runner = unittest.TextTestRunner()
    runner.run(suite)
