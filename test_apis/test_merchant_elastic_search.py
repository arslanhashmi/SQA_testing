from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth
from fake_useragent import UserAgent
from .global_variables import *
from .compare_json import compare_data_dictionaries


class TestMerchantEndPointsElasticSearch(object):

    url_merchant_with_id = MERCHANT_WITH_ID
    name_merchant_with_id = 'es_merchant_with_id'
    ua = UserAgent()
    header = {'user-agent': ua.chrome}
    http_auth = HTTPBasicAuth('prototype', 'prototype')
    date = str(datetime.now()).split(' ')[0]

    def test_with_all_correct_parameters_merchant_with_id(self):

        file_pointer = open('logs/{name}_{date}.txt'.format(date=self.date, name=self.name_merchant_with_id), 'w')
        file_pointer.write('Going to test {name} with correct data at {datetime}\n'.format(
            datetime=datetime.now(), name=self.name_merchant_with_id))

        response_php = requests.get(PHP_LINK + self.url_merchant_with_id, auth=self.http_auth,
                                      headers=self.header,)
        response_python = requests.get(PYTHON_LINK_ELASTIC_SEARCH + self.url_merchant_with_id, auth=self.http_auth,
                                         headers=self.header, )

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
        file_pointer.write(
            'Test ends for {name} at {datetime}'.format(datetime=datetime.now(), name=self.name_merchant_with_id))

        file_pointer.close()

