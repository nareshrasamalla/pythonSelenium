import logging
import re
from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    HOME_PAGE_TITLE_REGEX = re.compile(".*Welcome,.*")
    SEARCH_RESULT_REGEX = re.compile(".*You searched for.*")
    LOGOUT_TEXT = re.compile(".*User Login")
    SEARCH_CRITERIA = "PR3227019858"
    search = {"search": "PR3227019858",
              "submit": "Search"}
    login_credentials = {"username": "admin",
                         "password": "admin",
                         "submit": "Login "}
    @task
    def login(self):
        with self.client.post("/hms/", data=UserBehavior.login_credentials,
                              catch_response=True) as response_post:
            # logging.info(response_post.status_code)
            response_post.success()
            if response_post.status_code == 200:
                with self.client.get("/hms/master.php",
                                     catch_response=True) as response_get:
                    logging.info(response_get.status_code)
                    assert self.HOME_PAGE_TITLE_REGEX.search(response_get.text) is not None, \
                        "Expected title has not been found!"
                with self.client.post("/hms/search_registraion.php",
                                      UserBehavior.search,
                                      catch_response=True) as response_search:
                    logging.info(response_search.status_code)
                    with self.client.get(
                            "/hms/search_list.php?search=" + UserBehavior.SEARCH_CRITERIA + "&submit=Search",
                            catch_response=True)as response_result:
                        logging.info(response_result.status_code)
                        assert self.SEARCH_RESULT_REGEX.search(
                            response_result.text) is not None, "Expected Search result has not been found!"
                        self.client.get("/hms/logout.php")
            else:
                response_post.failure("/hms/" + ": returned " + str(response_post.status_code))


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = "http://selenium4testing.com"
    min_wait = 4500
    max_wait = 5000

