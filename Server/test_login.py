import requests
import allure
import json


""" Trip Yoetz Web """


class TestLogin:

    #1
    def test_valid_login(self):
        # API url :
        url = "https://trip-yoetz.herokuapp.com/auth/login"
        # Copy the body :
        body = {"email": "tsionalemayo73@gmail.com", "password": "123456"}
        # Send POST request :
        response = requests.post(url, data=body)
        print(response.content)
        # verify the status code:
        assert response.status_code == 200
        # verify how much time takes the response back:
        assert response.elapsed.total_seconds() < 3
        # Fetch the value:
        res = response.json()
        assert res["message"] == "login successful"
        assert res["success"] == True
        assert res["token"] is not None

        # Fetch value using Jsonpath:
        # json_response = json.loads(response.text)
        # message = jsonpath.jsonpath(json_response,"message")
        # print(message)
        # assert message == "login successful"
    #2
    def test_invalid_login_when_password_incorrect(self):
        url = "https://trip-yoetz.herokuapp.com/auth/login"
        body = {"email": "tsionalemayo73@gmail.com", "password": "12348"}
        response = requests.post(url, data=body)
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 3
        res = response.json()
        assert res["message"] == "password or email incorrect"

    #3
    def test_invalid_login_when_email_incorrect(self):
        url = "https://trip-yoetz.herokuapp.com/auth/login"
        body = {"email": "tsionalemayo73@gmai", "password": "123456"}
        response = requests.post(url, data=body)
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 3
        res = response.json()
        assert res["message"] == "no user found"
        # print(message)

    #4
    def test_invalid_login_when_email_is_null(self):
        url = "https://trip-yoetz.herokuapp.com/auth/login"
        body = {"password": "123456"}
        response = requests.post(url, data=body)
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 3
        res = response.json()
        assert res["message"] == "no user found"

    #5
    def test_invalid_login_when_password_is_null(self):
        url = "https://trip-yoetz.herokuapp.com/auth/login"
        body = {"email":"tsionalemayo73@gmail.com"}
        response = requests.post(url, data=body)
        assert response.status_code == 500
        assert response.elapsed.total_seconds() < 3
        res = response.json()
        assert res["message"] == "Illegal arguments: undefined, string"

    #6

    def test_invalid_login_when_email_and_password_are_null(self):
        url = "https://trip-yoetz.herokuapp.com/auth/login"
        body = {}
        response = requests.post(url, data=body)
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 3
        res = response.json()
        assert res["message"] == "no user found"






