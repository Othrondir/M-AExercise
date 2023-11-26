import requests

ENDPOINT = "https://petstore.swagger.io/v2"

def check_status_value(status):
    params = {"status": status}
    response = requests.get(ENDPOINT + "/pet/findByStatus", params=params)

    print(f"Request URL for status '{status}':", response.url)
    print("Response status code:", response.status_code)

    return response

def test_available_status():
    response = check_status_value("available")
    assert response.status_code == 200

def test_pending_status():
    response = check_status_value("pending")
    assert response.status_code == 200

def test_sold_status():
    response = check_status_value("sold")
    assert response.status_code == 200

def test_invalid_status_values():
    response = check_status_value("invalid")
    assert response.status_code == 400
