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
    ([("Україна", 603628, 41660900), ("Німеччина", 357022, 83166711), ("Італія", 301340, 60262770)], "Італія"),
    ([("Німеччина", 357022, 83166711), ("Італія", 301340, 60262770), ("Україна", 603628, 41660900)], "Італія"),
])
def test_sort_by_area(data, expected):
    # Тестуємо сортування за площею
    sorted_data = sort_by_area(data)
    assert sorted_data
