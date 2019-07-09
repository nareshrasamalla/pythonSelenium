class CreateUserTestData:
    api_create_user_url = "https://reqres.in/api/users"
    api_create_user_json = """{
        'name' : 'anti',
        'job' : 'programmer'
        'last_name' : 'sam'
     }"""


class WebPerformanceTestData:
    search = {"search": "PR3227019858",
              "submit": "Search"}
    login_credentials = {"username": "admin",
                         "password": "admin",
                         "submit": "Login "}
