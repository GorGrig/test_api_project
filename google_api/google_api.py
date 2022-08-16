import sys
sys.path.append("/home/hrayr/test_api_project")

from request.request_base import RequestBase


class GoogleMapsApi: 
    place_id = ""
    
    def __init__(self):
        self.BASE_URL = "https://rahulshettyacademy.com"
        self.KEY_FOR_ALL_REQUEST =  "?key=qaclick123" 
        self.request_base = RequestBase()
    
        
    def create_new_place(self):
        post_resours = "/maps/api/place/add/json"
        url = f"{self.BASE_URL}{post_resours}{self.KEY_FOR_ALL_REQUEST}"
        json_create_new_place_body = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362}, 
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"],
            "website": "http://google.com",
            "language": "French-IN"}
        result = self.request_base.post_request(url= url, body= json_create_new_place_body)
        status_code = self.request_base.get_status_code(result)
        field_status_value = self.request_base.get_values_from_json(result, ["status", "scope"])
        GoogleMapsApi.place_id = self.request_base.get_value_from_json(result, "place_id")
        return [status_code, field_status_value]
        
    def check_new_location(self, value, place_id):
        get_resours = "/maps/api/place/get/json"
        place = "&place_id="
        url = f"{self.BASE_URL}{get_resours}{self.KEY_FOR_ALL_REQUEST}{place}{place_id}"
        result = self.request_base.get_request(url)
        status_code = self.request_base.get_status_code(result)
        field_statu_value = self.request_base.get_value_from_json(result, value)
        return [status_code, field_statu_value]
    
    def change_new_location(self, place_id):
        put_resours =  "/maps/api/place/update/json"
        url = f"{self.BASE_URL}{put_resours}{self.KEY_FOR_ALL_REQUEST}"
        json_for_change_new_location = { 
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"}
        result = self.request_base.put_request(url, json_for_change_new_location)
        status_code = self.request_base.get_status_code(result)
        field_statu_value = self.request_base.get_value_from_json(result, "msg")
        return [status_code, field_statu_value]    
        
    def delete_new_location(self, place_id, value):
        delete_resours = "/maps/api/place/delete/json"
        url = f"{self.BASE_URL}{delete_resours}{self.KEY_FOR_ALL_REQUEST}"
        json_for_delete_location = {
            "place_id": place_id}
        result = self.request_base.delete_request(url, json_for_delete_location)
        status_code = self.request_base.get_status_code(result)
        field_statu_value = self.request_base.get_value_from_json(result, value)
        return [status_code, field_statu_value] 
