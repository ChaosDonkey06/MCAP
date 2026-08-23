import unittest

import mcap


class TestPackage(unittest.TestCase):
    def test_package_version(self):
        self.assertEqual(mcap.__version__, "0.1.0")


if __name__ == "__main__":
    unittest.main()
