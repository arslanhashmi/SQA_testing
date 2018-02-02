from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth
from fake_useragent import UserAgent
from .global_variables import *
import timeit
from .graph_functions import *


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

        file_pointer = open ( 'logs/{name}_{date}.txt'.format ( date=self.date, name=self.name ), 'w' )
        file_pointer.write ( 'Going to test API response timings for {name} with correct data at {datetime}\n'.format (
            datetime=datetime.now (), name=self.name ) )

        time_php = timeit.Timer (
            "requests.get('{PHP_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},)".format (
                UPDATED_LINK=self.url, header=self.header, PHP_LINK=PHP_LINK, ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_php = time_php.repeat ( API_HITS, 1 )

        time_python = timeit.Timer (
            "requests.get('{PYTHON_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},)".format (
                UPDATED_LINK=self.url, header=self.header, PYTHON_LINK=PYTHON_LINK ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_python = time_python.repeat ( API_HITS, 1 )

        file_pointer.write ( "Average time taken for {API_HITS} Php API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_php ) / len ( times_php ), '.4f' ) ) )
        file_pointer.write ( "Average time taken for {API_HITS} Python API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_python ) / len ( times_python ), '.4f' ) ) )

        file_pointer.close ()
        make_box_plot ( self.name, times_php, times_python )
        make_subplot ( self.name, times_php, times_python )
        assert True


    def test_with_all_correct_parameters_smiles_purchase(self):

        file_pointer = open ( 'logs/{name}_{date}.txt'.format ( date=self.date, name=self.name_smiles_purchase ), 'w' )
        file_pointer.write ( 'Going to test API response timings for {name} with correct data at {datetime}\n'.format (
            datetime=datetime.now (), name=self.name_smiles_purchase ) )

        time_php = timeit.Timer (
            "requests.post('{PHP_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header}, data={POST_DATA})".format (
                UPDATED_LINK=self.url_smiles_purchase, header=self.header, PHP_LINK=PHP_LINK,
                POST_DATA=POST_DATA_FOR_SMILES_PURCHASE ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_php = time_php.repeat ( API_HITS, 1 )
        time_python = timeit.Timer (
            "requests.post('{PYTHON_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header}, data={POST_DATA})".format (
                UPDATED_LINK=self.url_smiles_purchase, header=self.header, PYTHON_LINK=PYTHON_LINK,
                POST_DATA=POST_DATA_FOR_SMILES_PURCHASE ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_python = time_python.repeat ( API_HITS, 1 )

        file_pointer.write ( "Average time taken for {API_HITS} Php API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_php ) / len ( times_php ), '.4f' ) ) )
        file_pointer.write ( "Average time taken for {API_HITS} Python API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_python ) / len ( times_python ), '.4f' ) ) )

        file_pointer.close ()
        make_box_plot ( self.name_smiles_purchase, times_php, times_python )
        make_subplot ( self.name_smiles_purchase, times_php, times_python )
        assert True

