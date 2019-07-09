@api
Feature: User Creation
  Scenario: Creating an User using a Sample API
    Given URI for sample API
    When I perform POST and GET Requests
    Then i should see the Response Code and Response JSON