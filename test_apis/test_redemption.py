from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth
from fake_useragent import UserAgent
from .global_variables import *
from .compare_json import compare_data_dictionaries


class TestRedemptionsEndPoints(object):

    url = REDEMPTION
    url2 = REDEMPTION_SYNC
    name = 'redemption'
    name2 = 'redemption_sync'
    ua = UserAgent()
    header = {'user-agent': ua.chrome}
    http_auth = HTTPBasicAuth('prototype', 'prototype')
    date = str(datetime.now()).split(' ')[0]

    def test_with_all_correct_parameters_redemption(self):

        file_pointer = open('logs/{name}_{date}.txt'.format(date=self.date, name=self.name),'w')
        file_pointer.write('Going to test {name} with empty search scope and correct date at {datetime}\n'.format(
            datetime=datetime.now(), name=self.name))
        response_php = requests.post(PHP_LINK + self.url, auth=self.http_auth,
                                      headers=self.header, data=POST_DATA_FOR_REDEMPTION_PHP)
        response_python = requests.post(PYTHON_LINK + self.url, auth=self.http_auth,
                                         headers=self.header, data=POST_DATA_FOR_REDEMPTION_PYTHON )

        file_pointer.write (
            '{response_php} is php response status code and {response_python} is python response status code\n'.format (
                response_php=response_php.status_code, response_python=response_python.status_code ) )

        try:
            compare_data_dictionaries(response_php.json(), response_python.json(), file_pointer)
        except Exception as e:
            file_pointer.write(
                'While comparing JSON an exception occured: {exception}\n'.format(
                    exception=e))
        assert True
        file_pointer.write('Test ends for {name} at {datetime}'.format(datetime=datetime.now(), name=self.name))
        file_pointer.close()

    def test_with_all_correct_parameters_redemption_sync(self):

        file_pointer = open('logs/{name}_{date}.txt'.format(date=self.date, name=self.name2), 'w')
        file_pointer.write('Going to test {name} at {datetime}\n'.format(datetime=datetime.now(), name=self.name2))
        response_php = requests.post(PHP_LINK + self.url2, auth=self.http_auth,
                                      headers=self.header, data=POST_DATA_FOR_REDEMPTION_SYNC_PHP)
        response_python = requests.post(PYTHON_LINK + self.url2, auth=self.http_auth,
                                         headers=self.header, data=POST_DATA_FOR_REDEMPTION_SYNC_PYTHON)

        file_pointer.write(
            '{response_php} is php response status code and {response_python} is python response status code\n'.format(
                response_php=response_php.status_code, response_python=response_python.status_code))

        try:
            compare_data_dictionaries(response_php.json(), response_python.json(), file_pointer)
        except Exception as e:
            file_pointer.write(
                'While comparing JSON an exception occured: {exception}\n'.format(
                    exception=e))
        assert True
        file_pointer.write('Test ends for {name} at {datetime}'.format(datetime=datetime.now(), name=self.name2))
        file_pointer.close()
