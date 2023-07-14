import requests

import configuration

import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки


response_user = post_new_user(data.user_body);


# user_response = post_new_user(data.user_body)
# print(user_response.json()["authToken"])
# auth_token = user_response.json()["authToken"]
# print(auth_token)

def post_new_client_kit(kit_body, auth_token):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,  # подставляем полный url
                         json=kit_body,  # тут тело
                         headers={
                             "Content-Type": "application/json",
                             "Authorization": "Bearer" + auth_token
                         })  # а здесь должен отправляться полученный токене

# print(response)
