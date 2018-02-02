from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth
from fake_useragent import UserAgent
from .global_variables import *
from .compare_json import compare_data_dictionaries


class TestMerchantEndPoints(object):

    url_merchants = MERCHANTS #for merchants
    url_empty_search_scope = EMPTY_SEARCH_SCOPE_MODE
    url_merchant_search_scope = MERCHANT_SEARCH_SCOPE_MODE
    url_merchant_names = MERCHAT_NAMES
    url_merchant_name = MERCHAT_NAME
    url_merchant_with_id = MERCHANT_WITH_ID
    url_merchant_outlets_with_id = MERCHANT_OUTLETS_WITH_ID
    name_merchant_outlets_with_id = 'merchant_outlets_with_id'
    name_merchant_with_id = 'merchant_with_id'
    name_merchants = 'merchants'
    name_merchant_empty_search = 'merchant_empty_search_scope'
    name_merchant_search_scope = 'merchant_search_scope'
    name_merchant_names = 'merchant_names'
    name_merchant_name = 'merchant_name'
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
        response_python = requests.get(PYTHON_LINK + self.url_merchant_with_id, auth=self.http_auth,
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

    def test_with_all_correct_parameters_merchant_outlets_with_id(self):

            file_pointer = open('logs/{name}_{date}.txt'.format(date=self.date, name=self.name_merchant_outlets_with_id), 'w')
            file_pointer.write('Going to test {name} with correct data at {datetime}\n'.format(
                datetime=datetime.now(), name=self.name_merchant_outlets_with_id))

            response_php = requests.get(PHP_LINK + self.url_merchant_outlets_with_id, auth=self.http_auth,
                                          headers=self.header,)
            response_python = requests.get(PYTHON_LINK + self.url_merchant_outlets_with_id, auth=self.http_auth,
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
            file_pointer.write(
                'Test ends for {name} at {datetime}'.format(datetime=datetime.now(), name=self.name_merchant_outlets_with_id))
            file_pointer.close()

    def test_with_all_correct_parameters_merchant_name(self):

        file_pointer = open('logs/{name}_{date}.txt'.format ( date=self.date, name=self.name_merchant_name), 'w')
        file_pointer.write('Going to test {name} with correct data at {datetime}\n'.format(
            datetime=datetime.now(), name=self.name_merchant_name))

        response_php = requests.get(PHP_LINK + self.url_merchant_name, auth=self.http_auth,
                                      headers=self.header, )
        response_python = requests.get(PYTHON_LINK + self.url_merchant_name, auth=self.http_auth,
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
            'Test ends for {name} at {datetime}'.format(datetime=datetime.now(), name=self.name_merchant_name))
        file_pointer.close()

    def test_with_all_correct_parameters_merchant_names(self):

        file_pointer = open('logs/{name}_{date}.txt'.format(date=self.date, name=self.name_merchant_names ), 'w')
        file_pointer.write('Going to test {name} with correct data at {datetime}\n'.format(
            datetime=datetime.now(), name=self.name_merchant_names))

        response_php = requests.get(PHP_LINK + self.url_merchant_names, auth=self.http_auth,
                                      headers=self.header, )
        response_python = requests.get(PYTHON_LINK + self.url_merchant_names, auth=self.http_auth,
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
        file_pointer.write(
            'Test ends for {name} at {datetime}'.format(datetime=datetime.now(), name=self.name_merchant_names))
        file_pointer.close()

    def test_with_all_correct_parameters_merchant_search_scope(self):

        file_pointer = open('logs/{name}_{date}.txt'.format ( date=self.date, name=self.name_merchant_search_scope ), 'w')
        file_pointer.write('Going to test {name} with correct data at {datetime}\n'.format(
            datetime=datetime.now(), name=self.name_merchant_search_scope ) )

        response_php = requests.get ( PHP_LINK + self.url_merchant_search_scope, auth=self.http_auth,
                                      headers=self.header, )
        response_python = requests.get ( PYTHON_LINK + self.url_merchant_search_scope, auth=self.http_auth,
                                         headers=self.header, )

        file_pointer.write (
            '{response_php} is php response status code and {response_python} is python response status code\n'.format(
                response_php=response_php.status_code, response_python=response_python.status_code ) )
        try:
            compare_data_dictionaries ( response_php.json (), response_python.json (), file_pointer )
        except Exception as e:
            file_pointer.write (
                'While comparing JSON an exception occured: {exception}\n'.format (
                    exception=e ) )
        assert True
        file_pointer.write (
            'Test ends for {name} at {datetime}'.format(datetime=datetime.now(), name=self.name_merchant_search_scope))
        file_pointer.close ()

    def test_with_all_correct_parameters_merchants(self):

        file_pointer = open('logs/{name}_{date}.txt'.format(
            date=self.date, name=self.name_merchants),'w')
        file_pointer.write('Going to test {name} with correct data at {datetime}\n'.format(
            datetime=datetime.now (), name=self.name_merchants))

        response_php = requests.get(PHP_LINK + self.url_merchants, auth=self.http_auth,
                                      headers=self.header, )
        response_python = requests.get(PYTHON_LINK + self.url_merchants, auth=self.http_auth,
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
        file_pointer.write('Test ends for {name} at {datetime}'.format(datetime=datetime.now(), name=self.name_merchants))
        file_pointer.close()

    def test_with_all_correct_parameters_merchant_empty_search_scope(self):

            file_pointer = open('logs/{name}_{date}.txt'.format(
                date=self.date, name=self.name_merchant_empty_search), 'w')
            file_pointer.write('Going to test {name} with correct data at {datetime}\n'.format(
                datetime=datetime.now(), name=self.name_merchant_empty_search))

            response_php = requests.get(PHP_LINK + self.url_empty_search_scope, auth=self.http_auth,
                                          headers=self.header, )
            response_python = requests.get(PYTHON_LINK + self.url_empty_search_scope, auth=self.http_auth,
                                             headers=self.header,)

            file_pointer.write (
                '{response_php} is php response status code and {response_python} is python response status code\n'.format(
                    response_php=response_php.status_code, response_python=response_python.status_code))
            try:
                compare_data_dictionaries(response_php.json(), response_python.json(), file_pointer)
            except Exception as e:
                file_pointer.write(
                    'While comparing JSON an exception occured: {exception}\n'.format(
                        exception=e))
            assert True
            file_pointer.write('Test ends for {name} at {datetime}'.format(
                datetime=datetime.now(), name=self.name_merchant_empty_search))
            file_pointer.close()


