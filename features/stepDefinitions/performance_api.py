import logging

from locust import HttpLocust, TaskSequence, seq_task

logging.basicConfig(level=logging.INFO)


class TestingError(RuntimeError):
    pass


class userapi(TaskSequence):
    userapi_id = " "
    payload = """{
        "name" : "anti",
        "avatar" : "PyPerformance_POST",
        "last_name" : "sam"
    }"""

    @seq_task(1)
    def userapi_POST(self):
        self.response = self.client.post("/api/users", data=userapi.payload)
        json_response = self.r.json()
        logging.info("Post response : " + str(json_response))
        logging.info("Response status code: %s", self.r.status_code)
        logging.info("json : " + str(json_response))
        self.userapi_id = json_response.get("id")
        logging.info("User API ID :", self.userapi_id)

    @seq_task(2)
    def userapi_GET(self):
        self.r = self.client.get("/api/users/" + self.userapi_id)
        logging.info("Response status code: %s", self.r.status_code)


class getRequest(HttpLocust):
    task_set = userapi
    host = "https://reqres.in"
    min_wait = 1000
    max_wait = 5000
