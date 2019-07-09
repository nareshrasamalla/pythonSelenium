import os
from os.path import dirname


class GlobalVariables:
    global web_driver, project_path, feature_file_path, get_test_data, obj
    project_path = dirname(dirname(__file__))
    api_oid = "200"
    get_response = " "
    response_code = " "
    JSON_response = " "
    blank_data_response = " "
    invalid_data_response = " "
    screen_shot_path = os.path.join(project_path, r'screenshots')
    oid = " "
    fleetstream_id = " "
    vehicle_oid = " "
    updated_json_schema = " "


class Constants:
    CREATE_RESPONSE_CODE = 201
    SUCCESS_RESPONSE_CODE = 200
