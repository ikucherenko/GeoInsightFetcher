#!/usr/bin/env python3

import sys
import unittest
import requests
from exceptions import FileNotFoundException


def get_formatted_result(**to_print):
    """ Print formatted result
    :param to_print: the dictionary of params to print
    """
    result = list()
    result.append('=>-------------')
    for key, value in to_print.items():
        result.append('=> {0}: {1}'.format(key, value))
    result.append('=>-------------')
    return result


def find_info(city_name):
    """ Find results for city
    :arg city_name: name of the city
    :return dict of data about city or message that city is not found
    :raise Exception if city were not found
    """

    api = 'https://restcountries.eu/rest/v2/capital/{0}'.format(city_name.split(' ')[0].lower())

    response = requests.get(url=api)

    try:
        data = response.json()[0]

        return {
            'Country': data.get('name'),
            'Currency': data.get('currencies')[0].get('code'),
            'Country Population': data.get('population')
        }
    except KeyError:
        raise Exception('Invalid City Name')


def read_file(file_name):
    """ Read the file
    :arg file_name: name of file
    :return array of names of cities
    """
    result = list()
    try:
        with open(file_name, "r") as file:
            for line in file:
                result.append(line)
        return result
    except OSError as e:
        raise FileNotFoundException('File {0} is not found'.format(e.filename))


def print_help(script_name='madgicx_geo.py'):
    """ Print help method"""
    print('Usage: python {0} name_of_city or python {1} -f file_name'.format(script_name, script_name))
    print('Example:')
    print('python {0} San Francisco or python {1} -f cities.txt'.format(script_name, script_name))
    print('python {0} test (for tests execution)'.format(script_name))


def run_tests():
    """ Executes unittests """
    from test_madgicx_geo import TestGetFormattedResult

    class NullWriter(object):
        def write(*_, **__):
            pass

        def flush(*_, **__):
            pass

    def suit():
        tests = ['runTest']

        return unittest.TestSuite(map(TestGetFormattedResult, tests))

    results = unittest.TextTestRunner(stream=NullWriter()).run(suit())
    print('Failures {0}, Successfully {1}, Tests run {2}'
          .format(len(results.failures), results.wasSuccessful(), results.testsRun))


def main():

    # Get user input
    cities = []
    try:
        if sys.argv[1].lower() == 'test':
            run_tests()
            exit(0)
        if sys.argv[1].lower() == '-h' or sys.argv[1].lower() == '-help':
            print_help()
            exit(0)

        cities = ' '.join([str(x).title() for x in sys.argv[1:]]).split(', ') if sys.argv[1] != '-f' else \
            [city.title() for city in read_file(sys.argv[2])]
    except FileNotFoundException as fe:
        print(fe.message)
        print_help()
    except Exception as ex:
        print(ex)
        print_help()

    for city in cities:
        print('=> {0}'.format(city))
        try:
            result = find_info(city)

            for line in get_formatted_result(**result):
                print(line)
        except Exception as ex:
            print('=>-------------')
            print(ex)
            print('=>-------------')


if __name__ == '__main__':
    main()
