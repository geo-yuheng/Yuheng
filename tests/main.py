import unittest

if __name__ == "__main__":
    suite=unittest.TestSuite()
    suite.addTest(Load())
    runner=unittest.TextTestRunner()