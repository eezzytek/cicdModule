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