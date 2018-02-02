from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth
from fake_useragent import UserAgent
from .global_variables import *
import timeit
from .graph_functions import *


class TestInvalidIdEndPoints(object):
    name = 'invalid_id'
    url = INVALID_ID
    ua = UserAgent ()
    header = {'user-agent': ua.chrome}
    http_auth = HTTPBasicAuth('prototype', 'prototype')
    date = str(datetime.now()).split(' ')[0]

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




