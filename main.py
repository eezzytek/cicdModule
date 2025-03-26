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
    sort_type = 'площею' if by == 'area' else 'населенням'
    print(f"Сортування за {sort_type}:")
    for country in sorted_countries:
        name, area, population = country
        print(f"{name} - Площа: {area} кв.км, Населення: {population}")


# Вхід в програму
def main():
    file_path = "population_data.txt"
    countries = read_population_data(file_path)

    sorted_by_area = sort_by_area(countries)
    print_sorted_data(sorted_by_area, by="area")

    sorted_by_population = sort_by_population(countries)
    print_sorted_data(sorted_by_population, by="population")


if __name__ == "__main__":
    main()
