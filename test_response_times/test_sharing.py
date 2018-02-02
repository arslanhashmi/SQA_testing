from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth
from fake_useragent import UserAgent
from .global_variables import *
import timeit
from .graph_functions import *


class TestSharingEndPoints(object):

    url_send = SHARING_SEND_OFFERS
    url_receive = SHARING_RECEIVE_OFFERS

    name_send = 'sharing_send_offers'
    name_receive = 'sharing_receive_offers'
    ua = UserAgent()
    header = {'user-agent': ua.chrome}
    http_auth = HTTPBasicAuth('prototype', 'prototype')
    date = str(datetime.now()).split(' ')[0]

    def test_sending_with_all_correct_parameters(self):

        file_pointer = open ( 'logs/{name}_{date}.txt'.format ( date=self.date, name=self.name_send ), 'w' )
        file_pointer.write ( 'Going to test API response timings for {name} with correct data at {datetime}\n'.format (
            datetime=datetime.now (), name=self.name_send ) )

        time_php = timeit.Timer (
            "requests.get('{PHP_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},)".format (
                UPDATED_LINK=self.url_send, header=self.header, PHP_LINK=PHP_LINK, ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_php = time_php.repeat ( API_HITS, 1 )

        time_python = timeit.Timer (
            "requests.get('{PYTHON_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},)".format (
                UPDATED_LINK=self.url_send, header=self.header, PYTHON_LINK=PYTHON_LINK ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_python = time_python.repeat ( API_HITS, 1 )

        file_pointer.write ( "Average time taken for {API_HITS} Php API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_php ) / len ( times_php ), '.4f' ) ) )
        file_pointer.write ( "Average time taken for {API_HITS} Python API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_python ) / len ( times_python ), '.4f' ) ) )

        file_pointer.close ()
        make_box_plot ( self.name_send, times_php, times_python )
        make_subplot ( self.name_send, times_php, times_python )
        assert True

    def test_receiving_with_all_correct_parameters(self):

        file_pointer = open ( 'logs/{name}_{date}.txt'.format ( date=self.date, name=self.name_receive ), 'w' )
        file_pointer.write ( 'Going to test API response timings for {name} with correct data at {datetime}\n'.format (
            datetime=datetime.now (), name=self.name_receive ) )

        time_php = timeit.Timer (
            "requests.get('{PHP_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},)".format (
                UPDATED_LINK=self.url_receive, header=self.header, PHP_LINK=PHP_LINK, ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_php = time_php.repeat ( API_HITS, 1 )

        time_python = timeit.Timer (
            "requests.get('{PYTHON_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},)".format (
                UPDATED_LINK=self.url_receive, header=self.header, PYTHON_LINK=PYTHON_LINK ),
            "import requests; from requests.auth import HTTPBasicAuth", )
        times_python = time_python.repeat ( API_HITS, 1 )

        file_pointer.write ( "Average time taken for {API_HITS} Php API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_php ) / len ( times_php ), '.4f' ) ) )
        file_pointer.write ( "Average time taken for {API_HITS} Python API hits took: {average_time} secs\n".format (
            API_HITS=API_HITS, average_time=format ( sum ( times_python ) / len ( times_python ), '.4f' ) ) )

        file_pointer.close ()
        make_box_plot ( self.name_receive, times_php, times_python )
        make_subplot ( self.name_receive, times_php, times_python )
        assert True

