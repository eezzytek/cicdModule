import pytest
from main import read_population_data, sort_by_population, sort_by_area

@pytest.fixture
def mock_population_data():
    # Фікстура, яка повертає дані для тестування
    return [
        ("Україна", 1, 4),
        ("Німеччина", 2, 3),
        ("Італія", 3, 2)
    ]

@pytest.mark.parametrize("data, expected", [
    ([( "Україна", 603628, 41660900), ("Німеччина", 357022, 83166711)], "Україна"),
    ([( "Італія", 301340, 60262770), ("Німеччина", 357022, 83166711)], "Німеччина"),
])
def test_sort_by_area(data, expected):
    sorted_data = sort_by_area(data)
    assert sorted_data[0][0] == expected

def test_sort_by_population(mock_population_data):
    sorted_data = sort_by_population(mock_population_data)
    assert sorted_data[0][0] == "Ukraine"
    assert sorted_data[1][0] == "Italy"
    assert sorted_data[2][0] == "Germany"

def test_read_population_data():
    data = read_population_data('mock_population_data.txt')
    assert len(data) > 0  # Перевірка, що дані зчитано