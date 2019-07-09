import logging
import os
from os.path import dirname
from pytest_bdd import scenario, given, when, then
from pageObjects.page_tours import LoginTour
from utilities.base_ui import BaseUI
from utilities.global_variables import GlobalVariables

logging.basicConfig(level=logging.INFO)


class TestingError(RuntimeError):
    pass


base = BaseUI()
tours = LoginTour()
GlobalVariables.project_path = dirname(dirname(__file__))
GlobalVariables.feature_file_path = os.path.join(GlobalVariables.project_path, 'tours.feature')


@scenario(GlobalVariables.feature_file_path, 'To Verify Login functionality')
def test_to_verify_login_functionality():
    """To Verify Login functionality"""


@given('I navigate to web page')
def i_navigate_to_web_page():
    GlobalVariables.web_driver = base.launch_browser()
    logging.info('Chrome browser is launched')


@when('i enter email and password')
def i_enter_email_and_password():
    tours.username(GlobalVariables.web_driver)
    logging.info('Entered username')
    tours.password(GlobalVariables.web_driver)
    logging.info('Entered password')


@then('i click on login button')
def i_click_on_login_button():
    tours.submit(GlobalVariables.web_driver)
    logging.info('Clicked on login button')
