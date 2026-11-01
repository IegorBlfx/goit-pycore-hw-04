def get_cats_info(path):
    cats_info = []
    try:
        with open(path, "r", encoding="utf-8") as file:  # Open file with UTF-8 encoding
            for line in file:
                line = line.strip()  # Remove leading/trailing whitespace
                if not line:
                    continue
                try:
                    cat_id, name, age = line.split(",")  # Split line into id, name and age
                    cats_info.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    print(f"Пропущено некоректний рядок: {line}")
    except FileNotFoundError:  # Handle file not found error
        print(f"Файл не знайдено: {path}")
    return cats_info