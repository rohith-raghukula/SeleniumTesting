import requests

def test_login():
    login_url = 'https://profile.w3schools.com/log-in?redirect_url=https%3A%2F%2Fmy-learning.w3schools.com%2F'
    data = {'username': 'rohithr9701@gmail.com', 'password': 'rohith@120'}
    response = requests.post(login_url, data=data)
    
    assert response.status_code == 200
    assert 'Welcome' in response.text

def test_profile():
    profile_url = 'https://profile.w3schools.com/log-in?redirect_url=https%3A%2F%2Fmy-learning.w3schools.com%2F'
    response = requests.get(profile_url)
    
    assert response.status_code == 200
    assert 'My Profile' in response.text
