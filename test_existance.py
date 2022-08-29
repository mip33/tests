import pytest
from src.app import documents, check_document_existance

owners_map_fixture = [[x["number"], True] for x in documents]
owners_map_fixture.extend([
    ["test", False],
    ["test-2", False],
])


@pytest.mark.parametrize("number, is_valid", owners_map_fixture)
def test_check_document_existance(number: str, is_valid: bool):
    assert check_document_existance(number) == is_valid