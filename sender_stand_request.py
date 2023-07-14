from requests import post

from configuration import CREATE_USER_PATH, CREATE_KITS_PATH


def post_new_user(body: dict[str, str]):
    return post(
        CREATE_USER_PATH,
        json=body,
) 

def post_new_client_kit(kit_body: dict[str, str], auth_token: str):
    return post(
        CREATE_KITS_PATH,
        json=kit_body,
        headers={
            "Authorization": "Bearer" + auth_token
        }
    )

