import configuration
import requests


def test_positive_user_login():
    return requests.get(configuration.URL_SERVICE + "/test/abc123")
    response = test_positive_valid_user_login()
    assert response.status_code == 200

def test_negative_user_login():
    return requests.get(configuration.URL_SERVICE + "//")
    response = test_negative_user_login()
    assert response.status_code == 400

def test_negative_user():
    return requests.get(configuration.URL_SERVICE + "/3/abc123")
    response = test_negative_user()
    assert response.status_code == 400

def test_negative_login():
    return requests.get(configuration.URL_SERVICE + "/test/3")
    response = test_negative_login()
    assert response.status_code == 400