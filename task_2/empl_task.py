from typing import (
    List,
    Dict,
    Tuple
)

def work_employees(employees: List[Dict[str, any]]) -> str:
    """
    Обрабатывает список сотрудников и выполняет следующие операции:

    1. Определяет сотрудников с зарплатой > 50 000 и возвращает их имена.
    2. Вычисляет среднюю зарплату всех сотрудников без использования mean().
    3. Сортирует список сотрудников по убыванию зарплаты.

    :param employees: List[Dict[str, any]]
    :return: str
    """
    # генератор для сотрудников с зарплатой больше 50_000
    more_salary = (emp['name'] for emp in employees if emp['salary'] > 50_000)

    # подсчёт общей зарплаты и кол-ва сотрудников
    total_salary, count = 0, 0
    for emp in employees:
        total_salary += emp['salary']
        count += 1

    # средняя зарплата
    avg_salary = round(total_salary / count if count else 0)

    sorted_employees = sorted(employees, key=lambda emp: emp['salary'], reverse=True)

    more_salary_list = list(more_salary)

    sorted_employees_list = '\n'.join(
        (f"{emp['name']} - {emp['position']} - {emp['salary']}" for emp in sorted_employees))

    result = (f'Сотрудники с ЗП > 50 000: {more_salary_list}\n'
              f'Средняя зарплата: {avg_salary}\n'
              f'Сотрудники, отсортированные по ЗП: {sorted_employees_list}')

    return result

if __name__ == '__main__':
    employees = [
        {"name": "Иван", "position": "разработчик", "salary": 55000},
        {"name": "Анна", "position": "аналитик", "salary": 48000},
        {"name": "Петр", "position": "тестировщик", "salary": 52000},
    ]

    print(work_employees(employees))