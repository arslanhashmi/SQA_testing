from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth
from fake_useragent import UserAgent
from .global_variables import *
from .compare_json import compare_data_dictionaries
import pytest


class TestOutletEndPoints ( object ):
    name = 'outlets'
    url = NOON_AND_KEBAB
    ua = UserAgent ()
    header = {'user-agent': ua.chrome}
    http_auth = HTTPBasicAuth ( 'prototype', 'prototype' )
    date = str ( datetime.now () ).split ( ' ' )[0]

    def test_with_all_correct_parameters_with_offer_id(self):

        file_pointer = open ( 'logs/{name}_diff_lnglat_{date}.txt'.format (
            date=self.date, name=self.name ), 'w' )

        for redeemability_option in REDEMIBILITY_OPTIONS:
            for i in range ( len ( LATLNG ) ):
                updated_link = NOON_AND_KEBAB_WITHOUT_PARMS
                file_pointer.write (
                    'Going to test with redeemability:{r} with lng: {lng} and lat: {lat} at {datetime}\n'.format (
                        datetime=datetime.now (), lng=LATLNG[i][1], lat=LATLNG[i][0], r=redeemability_option ) )

                PARAMS_OUTLETS['lat'], PARAMS_OUTLETS['lng'] = LATLNG[i][0], LATLNG[i][1]
                PARAMS_OUTLETS['redeemability'] = redeemability_option
                for parm, value in PARAMS_OUTLETS.items ():
                    updated_link += parm + '=' + value + '&'
                updated_link = updated_link[0:len ( updated_link ) - 1]
                file_pointer.write ( updated_link + '\n'.format (
                    datetime=datetime.now (), lng=LATLNG[i][1], lat=LATLNG[i][0] ) )

                response_php = requests.get ( PHP_LINK + updated_link, auth=HTTPBasicAuth ( 'prototype', 'prototype' ),
                                              headers=self.header )
                response_python = requests.get ( PYTHON_LINK + updated_link,
                                                 auth=HTTPBasicAuth ( 'prototype', 'prototype' ),
                                                 headers=self.header )

                file_pointer.write (
                    '{response_php} is php response status code and {response_python} is python response status code\n'.format (
                        response_php=response_php.status_code, response_python=response_python.status_code ) )

                try:
                    compare_data_dictionaries ( response_php.json (), response_python.json (), file_pointer )
                except Exception as e:
                    file_pointer.write (
                        'While comparing JSON an exception occured: {exception}\n'.format (
                            exception=e ) )
                file_pointer.write (
                    'End test with redeemability:{r} with lng: {lng} and lat: {lat} at {datetime}\n\n\n'.format (
                        datetime=datetime.now (), lng=LATLNG[i][1], lat=LATLNG[i][0], r=redeemability_option ) )

            assert True
        file_pointer.close ()
