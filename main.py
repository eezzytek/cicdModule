# Зчитування даних з файлу
def read_population_data(file_path):
    countries = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                name, area, population = parts
                try:
                    area = float(area)
                    population = int(population)
                    countries.append((name, area, population))
                except ValueError:
                    print(f"Невірний формат даних у рядку: {line}")

    return countries

# Сортування за площею
def sort_by_area(countries):
    return sorted(countries, key=lambda x: x[1])

# Сортування за населенням
def sort_by_population(countries):
    return sorted(countries, key=lambda x: x[2])

# Виведення даних на екран
def print_sorted_data(sorted_countries, by="area"):
    print(f"Сортування за {'площею' if by == 'area' else 'населенням'}:")
    for country in sorted_countries:
        print(f"{country[0]} - Площа: {country[1]} кв.км, Населення: {country[2]}")