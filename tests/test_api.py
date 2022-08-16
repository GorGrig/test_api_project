import sys
sys.path.append("/home/hrayr/test_api_project")
from google_api.google_api import GoogleMapsApi


class TestGoogleAPI:
    
    def test_google_api_post(self):
        googleapi = GoogleMapsApi()
        result = googleapi.create_new_place()
        dictionary = result[1]
        assert result[0] == 200 and dictionary["status"] == "OK" and dictionary["scope"] == "APP"
    
    def test_google_api_get(self):
        googleapi = GoogleMapsApi()
        result = googleapi.check_new_location(value="website", place_id=GoogleMapsApi.place_id)
        assert result[0]  == 200 and result[1] ==  "http://google.com"
            
    def test_google_api_get_negative(self):
        googleapi = GoogleMapsApi()
        result = googleapi.check_new_location(value="msg", place_id="abracadabra")
        assert result[0]  == 404 and result[1] == "Get operation failed, looks like place_id  doesn't exists" 
                   
    def test_google_api_put(self):
        googleapi = GoogleMapsApi()
        result = googleapi.change_new_location(place_id=GoogleMapsApi.place_id)
        assert result[0]  == 200  and result[1] == "Address successfully updated" 
        
    def test_google_api_put_negative(self):
        googleapi = GoogleMapsApi()
        result = googleapi.change_new_location(place_id="abracadabra")
        assert result[0]  == 404  and result[1] == "Update address operation failed, looks like the data doesn't exists"
            
    def test_google_api_delete(self):
        googleapi = GoogleMapsApi()
        result = googleapi.delete_new_location(value="status", place_id=GoogleMapsApi.place_id)
        assert result[0]  == 200 and result[1] == "OK"
        
    def test_google_api_delete_negative(self):
        googleapi = GoogleMapsApi()
        result = googleapi.delete_new_location(value="msg", place_id="abracadabra")
        assert result[0]  == 404 and result[1] == "Delete operation failed, looks like the data doesn't exists"
