from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth
from fake_useragent import UserAgent
from .global_variables import *
import timeit
from .graph_functions import *


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

        file_pointer = open ( 'logs/{name}_{date}.txt'.format ( date=self.date, name=self.name_merchant_with_id ), 'w' )
        file_pointer.write ( 'Going to test API response timings for {name} with correct data at {datetime}\n'.format (
            datetime=datetime.now (), name=self.name_merchant_outlets_with_id ) )

        time_php = timeit.Timer (
            "requests.get('{PHP_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},)".format (
                UPDATED_LINK=self.url_merchant_with_id, header=self.header, PHP_LINK=PHP_LINK, ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_php = time_php.repeat ( API_HITS, 1 )

        time_python = timeit.Timer (
            "requests.get('{PYTHON_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},)".format (
                UPDATED_LINK=self.url_merchant_with_id, header=self.header, PYTHON_LINK=PYTHON_LINK ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_python = time_python.repeat ( API_HITS, 1 )

        file_pointer.write ( "Average time taken for {API_HITS} Php API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_php ) / len ( times_php ), '.4f' ) ) )
        file_pointer.write ( "Average time taken for {API_HITS} Python API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_python ) / len ( times_python ), '.4f' ) ) )

        file_pointer.close ()
        make_box_plot ( self.name_merchant_with_id, times_php, times_python )
        make_subplot ( self.name_merchant_with_id, times_php, times_python )

        assert True

    def test_with_all_correct_parameters_merchant_outlets_with_id(self):

        file_pointer = open ( 'logs/{name}_{date}.txt'.format ( date=self.date, name=self.name_merchant_outlets_with_id ), 'w' )
        file_pointer.write ( 'Going to test API response timings for {name} with correct data at {datetime}\n'.format (
            datetime=datetime.now (), name=self.name_merchant_outlets_with_id ) )

        time_php = timeit.Timer (
            "requests.get('{PHP_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},)".format (
                UPDATED_LINK=self.url_merchant_outlets_with_id, header=self.header, PHP_LINK=PHP_LINK, ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_php = time_php.repeat ( API_HITS, 1 )

        time_python = timeit.Timer (
            "requests.get('{PYTHON_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},)".format (
                UPDATED_LINK=self.url_merchant_outlets_with_id, header=self.header, PYTHON_LINK=PYTHON_LINK ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_python = time_python.repeat ( API_HITS, 1 )

        file_pointer.write ( "Average time taken for {API_HITS} Php API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_php ) / len ( times_php ), '.4f' ) ) )
        file_pointer.write ( "Average time taken for {API_HITS} Python API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_python ) / len ( times_python ), '.4f' ) ) )

        file_pointer.close ()
        make_box_plot ( self.name_merchant_outlets_with_id, times_php, times_python )
        make_subplot ( self.name_merchant_outlets_with_id, times_php, times_python )

        assert True

    def test_with_all_correct_parameters_merchant_name(self):

        file_pointer = open ( 'logs/{name}_{date}.txt'.format ( date=self.date, name=self.name_merchant_name ), 'w' )
        file_pointer.write ( 'Going to test API response timings for {name} with correct data at {datetime}\n'.format (
            datetime=datetime.now (), name=self.name_merchant_name ) )

        time_php = timeit.Timer (
            "requests.get('{PHP_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},)".format (
                UPDATED_LINK=self.url_merchant_name, header=self.header, PHP_LINK=PHP_LINK, ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_php = time_php.repeat ( API_HITS, 1 )

        time_python = timeit.Timer (
            "requests.get('{PYTHON_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},)".format (
                UPDATED_LINK=self.url_merchant_name, header=self.header, PYTHON_LINK=PYTHON_LINK ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_python = time_python.repeat ( API_HITS, 1 )

        file_pointer.write ( "Average time taken for {API_HITS} Php API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_php ) / len ( times_php ), '.4f' ) ) )
        file_pointer.write ( "Average time taken for {API_HITS} Python API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_python ) / len ( times_python ), '.4f' ) ) )

        file_pointer.close ()
        make_box_plot ( self.name_merchant_name, times_php, times_python )
        make_subplot ( self.name_merchant_name, times_php, times_python )

        assert True

    def test_with_all_correct_parameters_merchant_names(self):
        file_pointer = open ( 'logs/{name}_{date}.txt'.format ( date=self.date, name=self.name_merchant_names ), 'w' )
        file_pointer.write ( 'Going to test API response timings for {name} with correct data at {datetime}\n'.format (
            datetime=datetime.now (), name=self.name_merchant_names ) )

        time_php = timeit.Timer (
            "requests.get('{PHP_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},)".format (
                UPDATED_LINK=self.url_merchant_names, header=self.header, PHP_LINK=PHP_LINK, ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_php = time_php.repeat ( API_HITS, 1 )

        time_python = timeit.Timer (
            "requests.get('{PYTHON_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},)".format (
                UPDATED_LINK=self.url_merchant_names, header=self.header, PYTHON_LINK=PYTHON_LINK ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_python = time_python.repeat ( API_HITS, 1 )

        file_pointer.write ( "Average time taken for {API_HITS} Php API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_php ) / len ( times_php ), '.4f' ) ) )
        file_pointer.write ( "Average time taken for {API_HITS} Python API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_python ) / len ( times_python ), '.4f' ) ) )

        file_pointer.close ()
        make_box_plot ( self.name_merchant_names, times_php, times_python )
        make_subplot ( self.name_merchant_names, times_php, times_python )

        assert True

    def test_with_all_correct_parameters_merchant_search_scope(self):

        file_pointer = open ( 'logs/{name}_{date}.txt'.format ( date=self.date, name=self.name_merchant_search_scope ), 'w' )
        file_pointer.write ( 'Going to test API response timings for {name} with correct data at {datetime}\n'.format (
            datetime=datetime.now (), name=self.name_merchant_search_scope ) )

        time_php = timeit.Timer (
            "requests.get('{PHP_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},)".format (
                UPDATED_LINK=self.url_merchant_search_scope, header=self.header, PHP_LINK=PHP_LINK, ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_php = time_php.repeat ( API_HITS, 1 )

        time_python = timeit.Timer (
            "requests.get('{PYTHON_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},)".format (
                UPDATED_LINK=self.url_merchant_search_scope, header=self.header, PYTHON_LINK=PYTHON_LINK ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_python = time_python.repeat ( API_HITS, 1 )

        file_pointer.write ( "Average time taken for {API_HITS} Php API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_php ) / len ( times_php ), '.4f' ) ) )
        file_pointer.write ( "Average time taken for {API_HITS} Python API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_python ) / len ( times_python ), '.4f' ) ) )

        file_pointer.close ()
        assert True

    def test_with_all_correct_parameters_merchants(self):

        file_pointer = open ( 'logs/{name}_{date}.txt'.format ( date=self.date, name=self.name_merchants ), 'w' )
        file_pointer.write ( 'Going to test API response timings for {name} with correct data at {datetime}\n'.format (
            datetime=datetime.now (), name=self.name_merchants ) )

        time_php = timeit.Timer (
            "requests.get('{PHP_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},)".format (
                UPDATED_LINK=self.url_merchants, header=self.header, PHP_LINK=PHP_LINK, ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_php = time_php.repeat ( API_HITS, 1 )

        time_python = timeit.Timer (
            "requests.get('{PYTHON_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},)".format (
                UPDATED_LINK=self.url_merchants, header=self.header, PYTHON_LINK=PYTHON_LINK ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_python = time_python.repeat ( API_HITS, 1 )

        file_pointer.write ( "Average time taken for {API_HITS} Php API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_php ) / len ( times_php ), '.4f' ) ) )
        file_pointer.write ( "Average time taken for {API_HITS} Python API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_python ) / len ( times_python ), '.4f' ) ) )

        file_pointer.close ()
        make_box_plot ( self.name_merchants, times_php, times_python )
        make_subplot ( self.name_merchants, times_php, times_python )

        assert True

    def test_with_all_correct_parameters_merchant_empty_search_scope(self):
        file_pointer = open ( 'logs/{name}_{date}.txt'.format ( date=self.date, name=self.name_merchant_empty_search ), 'w' )
        file_pointer.write ( 'Going to test API response timings for {name} with correct data at {datetime}\n'.format (
            datetime=datetime.now (), name=self.name_merchant_empty_search ) )

        time_php = timeit.Timer (
            "requests.get('{PHP_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},)".format (
                UPDATED_LINK=self.url_empty_search_scope, header=self.header, PHP_LINK=PHP_LINK, ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_php = time_php.repeat ( API_HITS, 1 )

        time_python = timeit.Timer (
            "requests.get('{PYTHON_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},)".format (
                UPDATED_LINK=self.url_empty_search_scope, header=self.header, PYTHON_LINK=PYTHON_LINK ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_python = time_python.repeat ( API_HITS, 1 )

        file_pointer.write ( "Average time taken for {API_HITS} Php API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_php ) / len ( times_php ), '.4f' ) ) )
        file_pointer.write ( "Average time taken for {API_HITS} Python API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_python ) / len ( times_python ), '.4f' ) ) )

        file_pointer.close ()
        make_box_plot ( self.name_merchant_empty_search, times_php, times_python )
        make_subplot ( self.name_merchant_empty_search, times_php, times_python )

        assert True

