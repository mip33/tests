from os import environ
from dotenv import load_dotenv
import pytest
from ya_protocol import YandexProtocol

fixture_create_catalog = [
    ('new_catalog', 201),
    ('new_catalog_2', 201)
]


load_dotenv()

@pytest.mark.parametrize('catalog, code', fixture_create_catalog)
def test_create_catalog(catalog, code):
    yandex = YandexProtocol(environ.get("YANDEX_API_TOKEN"))
    result = yandex.create_folder(catalog)
    assert code == result.status_code


@pytest.mark.xfail
def test_create_catalog_error():
    yandex = YandexProtocol(environ.get("YANDEX_API_TOKEN"))
    result = yandex.create_folder('new_catalog_test')
    assert result.status_code == 201