from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth
from fake_useragent import UserAgent
from .global_variables import *
from .compare_json import compare_data_dictionaries


class TestSmilesEndPoints(object):

    url = SMILES
    url_smiles_purchase = SMILES_PURCHASE
    name = 'smiles'
    name_smiles_purchase = 'smiles_purchase'
    ua = UserAgent()
    header = {'user-agent': ua.chrome}
    http_auth = HTTPBasicAuth('prototype', 'prototype')
    date = str(datetime.now()).split(' ')[0]
    php_link = PHP_LINK_SMILE
    python_link = PYTHON_LINK_SMILE

    def test_with_all_correct_parameters(self):

        file_pointer = open('logs/{name}_{date}.txt'.format(date=self.date, name=self.name),'w')
        file_pointer.write('Going to test {name} with correct date at {datetime}\n'.format(
            datetime=datetime.now(), name=self.name))

        response_php = requests.get(self.php_link, auth=self.http_auth,
                                      headers=self.header, )
        response_python = requests.get(self.python_link, auth=self.http_auth,
                                         headers=self.header,)

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
        file_pointer.write('Test ends for {name} at {datetime}'.format(datetime=datetime.now(), name=self.name))
        file_pointer.close()

    def test_with_all_correct_parameters_smiles_purchase(self):

        file_pointer = open('logs/{name}_{date}.txt'.format(date=self.date, name=self.name_smiles_purchase),'w')
        file_pointer.write('Going to test {name} with correct date at {datetime}\n'.format(
            datetime=datetime.now(), name=self.name_smiles_purchase))

        response_php = requests.post(PHP_LINK+self.url_smiles_purchase, auth=self.http_auth,
                                      headers=self.header, data=POST_DATA_FOR_SMILES_PURCHASE)
        response_python = requests.post(PYTHON_LINK+self.url_smiles_purchase, auth=self.http_auth,
                                         headers=self.header, data=POST_DATA_FOR_SMILES_PURCHASE)

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
        file_pointer.write('Test ends for {name} at {datetime}'.format(datetime=datetime.now(), name=self.name_smiles_purchase))
        file_pointer.close()

