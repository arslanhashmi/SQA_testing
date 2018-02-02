from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth
from fake_useragent import UserAgent
from .global_variables import *
from .compare_json import compare_data_dictionaries
import pytest


class TestOutletEndPointsElasticSearch(object):
    name = 'es_outlets'
    url = NOON_AND_KEBAB
    ua = UserAgent()
    header = {'user-agent': ua.chrome}
    http_auth = HTTPBasicAuth('prototype', 'prototype')
    date = str(datetime.now()).split(' ')[0]


    def test_with_all_correct_parameters(self):

        file_pointer = open('logs/{name}_{date}.txt'.format(date=self.date, name=self.name), 'w')
        file_pointer.write('Going to test {name} with correct date at {datetime}\n'.format(
            datetime=datetime.now(), name=self.name))
        response_php = requests.get(PHP_LINK + self.url, auth=self.http_auth,
                                      headers=self.header)
        response_python = requests.get(PYTHON_LINK_ELASTIC_SEARCH + self.url, auth=self.http_auth,
                                         headers=self.header)

        file_pointer.write (
            '{response_php} is php response status code and {response_python} is python response status code\n'.format(
                response_php=response_php.status_code, response_python=response_python.status_code))

        try:
            compare_data_dictionaries(response_php.json(), response_python.json(), file_pointer)
        except Exception as e:
            file_pointer.write(
                'While comparing JSON an exception occured: {exception}\n'.format(
                    exception=e))
        file_pointer.write('Test ends for {name} with correct date at {datetime}'.format(
            datetime=datetime.now(), name=self.name))
        assert True
        file_pointer.close()

    @pytest.mark.redem_option
    def test_with_missing_arguments(self):

        file_pointer = open('logs/{name}_less_keys_not_redeemable_{date}.txt'.format(
            date=self.date, name=self.name), 'w')



        for parameter in KEYS_OUTLETS:
            updated_link = NOON_AND_KEBAB_WITHOUT_PARMS
            file_pointer.write('Going to test {name} with skiping {parameter} at {datetime}\n'.format(
                datetime=datetime.now(),parameter=parameter, name=self.name))
            skip_parm = [parameter]
            for parm, value in PARAMS_OUTLETS.items():
                if parm not in skip_parm:
                    updated_link += parm + '=' + value + '&'
            updated_link = updated_link[0:len(updated_link) - 1]

            response_php = requests.get(PHP_LINK + updated_link, auth=HTTPBasicAuth('prototype', 'prototype'),
                                        headers=self.header)
            response_python = requests.get(PYTHON_LINK_ELASTIC_SEARCH + updated_link, auth=HTTPBasicAuth('prototype', 'prototype'),
                                           headers=self.header)

            file_pointer.write (
                '{response_php} is php response status code and {response_python} is python response status code\n'.format (
                    response_php=response_php.status_code, response_python=response_python.status_code ) )

            try:
                compare_data_dictionaries(response_php.json (), response_python.json (), file_pointer)
            except Exception as e:
                file_pointer.write(
                    'While comparing JSON an exception occured: {exception}\n'.format(
                        exception=e))
            file_pointer.write('Test ends for {name} with skiping {parameter} at {datetime}\n\n'.format(
                datetime=datetime.now(),parameter=parameter, name=self.name))
        assert True
        file_pointer.close()


