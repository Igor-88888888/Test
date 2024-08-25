import configuration
import data
import requests


def get_aut_user():
    return requests.get(configuration.URL_SERVICE + configuration.LOGS_USER_SYSTEM)

def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER,
                         json=user_body)