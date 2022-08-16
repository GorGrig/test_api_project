import sys
sys.path.append("/home/hrayr/test_api_project")

import requests



class RequestBase:
    
    def __init__(self, headers = {"Content-Type" : "application/json" }, cookies = "") -> None:
        self.headers = headers
        self.cookies = cookies
    
    def get_request(self, url : str):
        result = requests.get(url, headers=self.headers, cookies=self.cookies)
        return result
       
    def post_request(self, url : str, body):
            result = requests.post(url, json=body, headers=self.headers, cookies=self.cookies)
            return result
        
    def put_request(self, url : str, body):
        result = requests.put(url, json=body, headers=self.headers, cookies=self.cookies)
        return result
    
    def delete_request(self, url : str, body):
        result = requests.delete(url, json=body, headers=self.headers, cookies=self.cookies)
        return result
    
    def get_status_code(self, result_from_requests) -> int:
        return result_from_requests.status_code
    
    def get_value_from_json(self, result_from_requests, name_field : str) -> str:
        result_request = result_from_requests.json()
        return result_request.get(name_field)
    
    def get_values_from_json(self, result_from_requests, names_field_with_string_type : list ) -> dict:
        key_value = {}
        result_request = result_from_requests.json()
        for i in names_field_with_string_type:
            key_value[i] = result_request.get(i)
        return key_value
    