import data

import sender_stand_request

def get_new_user_token():
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.user_body.copy()
    #отпарвляем запрос
    user_response = sender_stand_request.post_new_user(current_body)
    #получем и выделяем токен
    auth_token = user_response.json()["authToken"]

def get_kit_body(name):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    kit_current_body = data.kit_body.copy()
    # изменение значения в поле name
    kit_current_body["name"] = name
    # возвращается новый словарь с нужным значением name
    return kit_current_body
# print(data.user_body.copy())

def positive_assert(name):
    # В переменную kit_body  сохраняется обновленное тело запроса
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body,auth_token)
    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201
    #проверяем что предпнное  совпадает с отправленным
    assert kit_response.json()["name"] == name

def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")