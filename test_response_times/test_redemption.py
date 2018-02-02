from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth
from fake_useragent import UserAgent
from .global_variables import *
import timeit
from .graph_functions import *


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

        file_pointer = open ( 'logs/{name}_{date}.txt'.format ( date=self.date, name=self.name ), 'w' )
        file_pointer.write ( 'Going to test API response timings for {name} with correct data at {datetime}\n'.format (
            datetime=datetime.now (), name=self.name ) )

        time_php = timeit.Timer (
            "requests.post('{PHP_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header}, data={POST_DATA_FOR_REDEMPTION_SYNC_PHP})".format (
                UPDATED_LINK=self.url, header=self.header, PHP_LINK=PHP_LINK,
                POST_DATA_FOR_REDEMPTION_SYNC_PHP=POST_DATA_FOR_REDEMPTION_PHP ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_php = time_php.repeat ( API_HITS, 1 )
        time_python = timeit.Timer (
            "requests.post('{PYTHON_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header}, data={POST_DATA_FOR_REDEMPTION_SYNC_PHP})".format (
                UPDATED_LINK=self.url, header=self.header, PYTHON_LINK=PYTHON_LINK,
                POST_DATA_FOR_REDEMPTION_SYNC_PHP=POST_DATA_FOR_REDEMPTION_PYTHON ),
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


    def test_with_all_correct_parameters_redemption_sync(self):
        file_pointer = open ( 'logs/{name}_{date}.txt'.format ( date=self.date, name=self.name2 ), 'w' )
        file_pointer.write ( 'Going to test API response timings for {name} with correct data at {datetime}\n'.format (
            datetime=datetime.now (), name=self.name2 ) )

        time_php = timeit.Timer (
            "requests.post('{PHP_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header}, data={POST_DATA_FOR_REDEMPTION_SYNC_PHP})".format (
                UPDATED_LINK=self.url2, header=self.header, PHP_LINK=PHP_LINK,
                POST_DATA_FOR_REDEMPTION_SYNC_PHP=POST_DATA_FOR_REDEMPTION_SYNC_PHP ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_php = time_php.repeat ( API_HITS, 1 )
        time_python = timeit.Timer (
            "requests.post('{PYTHON_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header}, data={POST_DATA_FOR_REDEMPTION_SYNC_PHP})".format (
                UPDATED_LINK=self.url2, header=self.header, PYTHON_LINK=PYTHON_LINK,
                POST_DATA_FOR_REDEMPTION_SYNC_PHP=POST_DATA_FOR_REDEMPTION_SYNC_PHP ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_python = time_python.repeat ( API_HITS, 1 )

        file_pointer.write ( "Average time taken for {API_HITS} Php API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_php ) / len ( times_php ), '.4f' ) ) )
        file_pointer.write ( "Average time taken for {API_HITS} Python API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_python ) / len ( times_python ), '.4f' ) ) )

        file_pointer.close ()
        make_box_plot ( self.name2, times_php, times_python )
        make_subplot ( self.name2, times_php, times_python )
        assert True
