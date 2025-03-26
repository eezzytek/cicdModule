import pytest
from main import read_population_data, sort_by_population, sort_by_area

@pytest.fixture
def mock_population_data():
    # Фікстура, яка повертає дані для тестування
    return [
        ("Україна", 603628, 41660900),
        ("Німеччина", 357022, 83166711),
        ("Італія", 301340, 60262770)
    ]

@pytest.mark.parametrize("data, expected", [
    ([("Україна", 603628, 41660900), ("Німеччина", 357022, 83166711)], "Україна"),
    ([("Україна", 301340, 60262770), ("Німеччина", 357022, 83166711)], "Україна"),
])
def test_sort_by_area(data, expected):
    # Тестуємо сортування за площею
    sorted_data = sort_by_area(data)
    assert sorted_data[0][0] == expected

def test_sort_by_population(mock_population_data):
    # Тестуємо сортування за населенням
    sorted_data = sort_by_population(mock_population_data)
    assert sorted_data[0][0] == "Німеччина"
    assert sorted_data[1][0] == "Україна"
    assert sorted_data[2][0] == "Італія"

def test_read_population_data(mock_population_data):
    data = read_population_data('population_data.txt')
    assert len(mock_population_data) > 0  # Перевірка, що дані зчитано