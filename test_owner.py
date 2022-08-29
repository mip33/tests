import pytest
from unittest.mock import patch
from src.app import documents, get_doc_owner_name, get_all_doc_owners_names

owners_map = [
    ["2207 876234", "Василий Гупкин"],
    ["11-2", "Геннадий Покемонов"],
    ["10006", "Аристарх Павлов"],
]


@pytest.mark.parametrize("code,name", owners_map)
def test_get_doc_owner_name(code: str, name: str):
    with patch('builtins.input', return_value=code):
        assert get_doc_owner_name() == name


def test_get_doc_owner_name_invalid():
    with patch('builtins.input', return_value="xxx"):
        assert get_doc_owner_name() is None


def test_get_all_doc_owners_names():
    expected = [x["name"] for x in documents]

    assert sorted(get_all_doc_owners_names()) == sorted(expected)