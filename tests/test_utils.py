from unittest.mock import mock_open, patch

from src.utils import get_classes_from_json, load_json_data


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"name": "Телевизоры","description": "Современный телевизор","products": '
    '[{"name": "55 QLED 4K","description": "Фоновая подсветка","price": 123000, "quantity": 7}]}]',
)
def test_get_json_data(mock_open, mock_categories):
    json_data = load_json_data("fake_path")
    assert json_data == mock_categories


def test_get_classes_from_json_1(mock_categories):
    assert get_classes_from_json(mock_categories)[0].name == "Телевизоры"


def test_get_classes_from_json_2(capsys, mock_categories):
    get_classes_from_json(mock_categories)[0].products
    message = capsys.readouterr()
    assert message.out.strip() == "55 QLED 4K, 7 руб. Остаток: 123000"


def test_get_classes_from_json_4():
    assert get_classes_from_json([]) == []


def test_get_classes_from_json_5():
    assert get_classes_from_json(None) == []
