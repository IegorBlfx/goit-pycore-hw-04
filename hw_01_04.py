def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    _, salary = line.split(",")
                    total += float(salary)
                    count += 1
                except ValueError:
                    print(f"Пропущено некоректний рядок: {line}")
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return 0, 0

    average = total / count if count > 0 else 0
    return total, average
