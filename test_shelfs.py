from unittest.mock import patch

import pytest

from src.app import directories, documents, remove_doc_from_shelf, add_new_shelf, append_doc_to_shelf, delete_doc, \
    get_doc_shelf, move_doc_to_shelf, show_document_info, add_new_doc


def test_remove_doc_from_shelf():
    doc_number = documents[0]["number"]
    shelf_number = directories['1']

    before = len(shelf_number)
    remove_doc_from_shelf(doc_number)
    after = len(shelf_number)

    assert after < before


def test_add_new_shelf_with_arg():
    before = len(directories)
    add_new_shelf("new shelf")
    after = len(directories)

    assert before < after


def test_add_new_shelf_without_arg():
    before = len(directories)
    with patch('builtins.input', return_value="xxx"):
        add_new_shelf()
    after = len(directories)

    assert before < after


def test_append_doc_to_shelf():
    doc_number, shelf_number = documents[0]["number"], "1"
    before = len(directories[shelf_number])
    append_doc_to_shelf(doc_number, shelf_number)
    after = len(directories[shelf_number])

    assert before < after


def test_delete_doc():
    before = len(documents)
    with patch('builtins.input', return_value=documents[0]["number"]):
        delete_doc()
    after = len(documents)

    assert before > after


def test_get_doc_shelf():
    with patch('builtins.input', return_value=documents[0]["number"]):
        shelf_number = get_doc_shelf()

    assert shelf_number == "1"


def test_move_doc_to_shelf():
    doc_number = documents[0]["number"]
    orig_shelf_number = "1"
    dest_shelf_number = "2"

    with patch('builtins.input', side_effect=[doc_number, dest_shelf_number]):
        move_doc_to_shelf()

    assert doc_number not in directories[orig_shelf_number]
    assert doc_number in directories[dest_shelf_number]


def test_show_document_info():
    doc = {
        "type": "type1",
        "number": "number1",
        "name": "name1"
    }

    expected = f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"'

    assert expected == show_document_info(doc)


def test_add_new_doc():
    doc_number = "777"
    shelf_number = "1"

    return_values = [doc_number, "passport", "Test User", shelf_number]

    with patch("builtins.input", side_effect=return_values):
        add_new_doc()

    expected = {
        "type": return_values[1],
        "number": doc_number,
        "name": return_values[2]
    }

    assert expected in documents
    assert doc_number in directories[shelf_number]