from Api_Testing.api_class import API_testing
import json


class Test_Api_server:
    url = "https://652645bb917d673fd76bed89.mockapi.io/Automation_testing"

    # Check status code
    def test_status_code(self):
        data = API_testing(self.url).status_code()
        assert data == 200

    # test case for POST method
    def test_post_method(self):
        data = {"Name": "priya", "City": "chennai", "Country": "India"}
        assert API_testing(self.url).insert_data(data) == 201

    # test case for Update method
    def test_update_method(self):
        data = {"Name": "Riya"}
        response = API_testing(self.url).update_data(id=9, json_data=data)
        assert response == 200

    # test case for DELETE method
    def test_delete_method(self):
        response = API_testing(self.url).delete_data(10)
        print(response)
