def total_salary(path: str):
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = []
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    try:
                        salary = int(parts[1])
                        salaries.append(salary)
                    except ValueError:
                        print(f"Некоректне значення зарплати у рядку: {line}")
            if not salaries:
                return 0, 0
            total = sum(salaries)
            average = total // len(salaries)
            return total, average
    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")







def get_cats_info(path: str):
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    cat_id, name, age = parts
                    cats.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
        return cats
    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []


cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)




































