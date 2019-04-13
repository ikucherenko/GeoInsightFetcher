import unittest
from app.madgicx_geo import get_formatted_result, print_help
from unittest.mock import patch, call


class TestGetFormattedResult(unittest.TestCase):
    def runTest(self):
        result = get_formatted_result(**{'City': 'Kiev', 'Currency': 'HRY'})
        self.assertEqual(result[0], '=>-------------')
        self.assertEqual(result[3], '=>-------------')


class TestGetHelp(unittest.TestCase):
    def runTest(self):
        with unittest.mock.patch('builtins.print') as mocked_print:
            print_help()
            self.assertEqual(mocked_print.mock_calls,[
                call('Usage: python madgicx_geo.py name_of_city or python madgicx_geo.py -f file_name'),
                call('Example:'),
                call('python madgicx_geo.py San Francisco or python madgicx_geo.py -f cities.txt'),
                call('python madgicx_geo.py test (for tests execution)')])


class TestGetHelpWithParams(unittest.TestCase):
    def runTest(self):
        with unittest.mock.patch('builtins.print') as mocked_print:
            print_help('test.py')
            self.assertEqual(mocked_print.mock_calls,[
                call('Usage: python test.py name_of_city or python test.py -f file_name'),
                call('Example:'),
                call('python test.py San Francisco or python test.py -f cities.txt'),
                call('python test.py test (for tests execution)')])
