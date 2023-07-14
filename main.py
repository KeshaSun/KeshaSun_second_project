from create_kit_name_kit_test import get_new_user_token, positive_assert

# Вот такое надо делать в тестах, но лучше один зраз запросить токен в начале тестов, в потом прокидывать его во все тесты
token = get_new_user_token()
positive_assert('Мой набор', token)


# Пример тестов c правильным получением токена

def test_1(anything, token):
    print('test_1', anything, token)

def test_2(anything, token):
    print('test_2', anything, token)

def run_all_tests():
    token = get_new_user_token()

    test_1(token)
    test_2(token)