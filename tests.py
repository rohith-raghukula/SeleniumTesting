import requests

def test_web_page():
    url = 'https://www.example.com/'
    response = requests.get(url)
    
    assert response.status_code == 200
    assert 'Example Domain' in response.text
