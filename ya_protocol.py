import requests



class YandexProtocol:
    token: str
    headers: dict

    def __init__(self, token) -> None:
        self.token = token
        self.headers = {'Authorization': f'OAuth {token}'}

        assert self.token != "", "Укажите токен для работы с API YANDEX"


    def create_folder(self, target_folder):
        url = 'https://cloud-api.yandex.net/v1/disk/resources?path=' + target_folder
        response = requests.put(url, headers=self.headers)
        return  response

