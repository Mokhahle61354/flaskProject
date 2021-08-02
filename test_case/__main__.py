from test_case.yandex_functions import TestYandexFunctions
from test_case.end_point import TestPages
import unittest

def suite():
    suite = unittest.TestSuite()
    suite.addTest(
        test = TestPages(methodName="test_distance_instance")
    )

    suite.addTest(
        test = TestPages(methodName="test_enclosed_logic")
    )

    suite.addTest(
        test = TestYandexFunctions(methodName="check_geo_object")
    )
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
