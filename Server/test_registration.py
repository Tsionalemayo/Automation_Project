import requests
import random

class TestRegstration:

    def test_valid_registration(self):
        url = "https://trip-yoetz.herokuapp.com/auth/register"
        body ={"name":"Tsiona",
               "lastName":"Alemayo",
               "birthDate":"1994-07-03",
               "email":f"tsio@gmail.com{random.randint(1,100)}",
              "password":"54321"}
        response = requests.post(url, data=body)
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 3
        res = response.json()
        assert res["message"] == "user added successfully"


    def test_invalid_registration_with_exists_email(self):
        url = "https://trip-yoetz.herokuapp.com/auth/register"
        body = {"name": "Tsiona", "lastName": "Alemayo", "birthDate": "1994-07-03", "email": "tsio@gmail.com",
                "password": "54321"}
        response = requests.post(url, data=body)
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 3
        res = response.json()
        assert res["message"] == "user with that email already exists"




