import logging
import os
from os.path import dirname

import requests
import json
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from utilities.testdata import CreateUserTestData
from utilities.global_variables import GlobalVariables

logging.basicConfig(level=logging.INFO)

GlobalVariables.project_path = dirname(dirname(__file__))
GlobalVariables.feature_file_path = os.path.join(GlobalVariables.project_path, "user_creation.feature")


class TestingError(RuntimeError):
    pass


@scenario(GlobalVariables.feature_file_path, 'Creating an User using a Sample API')
def test_creating_an_user_using_a_sample_api():
    """Creating an User using a Sample API."""


@given('URI for sample API')
def uri_for_sample_api():
    """URI for sample API."""
    logging.info("URI for api is : %s", CreateUserTestData.api_create_user_url)


@when('I perform POST and GET Requests')
def i_perform_post_and_get_requests():
    """I perform POST and GET Requests."""
    GlobalVariables.response_code = requests.post(CreateUserTestData.api_create_user_url,
                                                  data=CreateUserTestData.api_create_user_json)
    post_json_response = GlobalVariables.response_code.json()
    logging.info("JSON Response for POST request is : %s", post_json_response)
    o_id = post_json_response.get("id")
    logging.info("OID is %s : ", o_id)
    GlobalVariables.get_response = requests.get(CreateUserTestData.api_create_user_url + o_id)
    get_json_response = GlobalVariables.get_response.json()
    logging.info("JSON Response for GET request is : %s", json.dumps(get_json_response, indent=4))


@then('i should see the Response Code and Response JSON')
def i_should_see_the_response_code_and_response_json():
    """i should see the Response Code and Response JSON."""
    logging.info("Response code for POST Request is : %s", GlobalVariables.response_code)
    logging.info("Response code for GET Request with OID is : %s", GlobalVariables.get_response)
