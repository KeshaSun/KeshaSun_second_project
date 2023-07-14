import data

from sender_stand_request import post_new_user, post_new_client_kit

def get_new_user_token():
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.user_body.copy()
    #отпарвляем запрос
    user_response = post_new_user(current_body).json()
    #получем и возвращаем токен
    return user_response['authToken']
    

def get_kit_body(name: str):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    kit_current_body = data.kit_body.copy()
    print(kit_current_body)
    # изменение значения в поле name
    kit_current_body["name"] = name
    # возвращается новый словарь с нужным значением name
    return kit_current_body

def positive_assert(name: str, auth_token: str):
    # В переменную kit_body  сохраняется обновленное тело запроса
    kit_body = get_kit_body(name)
    kit_response = post_new_client_kit(kit_body, auth_token)
    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201
    #проверяем что предпнное  совпадает с отправленным
    assert kit_response.json()["name"] == name
