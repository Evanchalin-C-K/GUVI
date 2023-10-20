# File contains API server methods

import requests


class API_testing:
    def __init__(self, api_server_url):
        self.url = api_server_url

    # fetch data from the API server
    def fetch_data(self):
        response = requests.get(self.url)
        return response.json()

    # get the status code of API server
    def status_code(self):
        return requests.get(self.url).status_code

    # insert data to the API server
    def insert_data(self, json_data):
        response = requests.post(self.url, data=json_data)
        return response.status_code

    # update data in the API server
    def update_data(self, id, json_data):
        id = str(id)
        url = self.url + "/" + id
        for data in self.fetch_data():
            if data['id'] == id:
                response = requests.put(url, data=json_data)
                print(response)
                return response.status_code

    # delete data from the API server
    def delete_data(self, id):
        id = str(id)
        url = self.url + "/" + id
        for data in self.fetch_data():
            if data['id'] == id:
                response = requests.delete(url)
                return response.status_code
