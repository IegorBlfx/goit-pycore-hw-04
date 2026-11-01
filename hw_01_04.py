def total_salary(path): # Function to calculate total and average salary from a file
    total = 0
    count = 0
    try:
        with open(path, "r", encoding="utf-8") as file: # Open file with UTF-8 encoding
            for line in file:
                line = line.strip()   # Remove leading/trailing whitespace
                if not line:
                    continue
                try:
                    _, salary = line.split(",") # Split line into name and salary
                    total += float(salary)
                    count += 1
                except ValueError:
                    print(f"Пропущено некоректний рядок: {line}")
    except FileNotFoundError:  # Handle file not found error
        print(f"Файл не знайдено: {path}")
        return 0, 0

    average = total / count if count > 0 else 0
    return total, average
