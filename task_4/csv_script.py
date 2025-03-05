import csv
from task_1.crud_script import DatabaseHandler
from typing import (
    List,
    Tuple
)

class ChildDatabaseHandler(DatabaseHandler):
    def read_csv(self, file_path: str) -> List[Tuple[str, str, int]]:
        """
        Чтение данных из CSV-файла

        :param file_path: str
        :return: List[Tuple[str, str, int]]
        """
        employees = []
        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader) # пропустим заголовок
            for row in reader:
                name, position, salary = row
                employees.append((name, position, int(salary)))
        return employees

    def write_csv_db(self, file_path: str) -> None:
        """
        Запись данных из CSV в базу данных

        :param file_path: str
        :return: None
        """
        employees = self.read_csv(file_path)
        self.cursor.executemany(
            'INSERT INTO employees (name, position, salary) VALUES (%s, %s, %s)',
            employees
        )
        self.conn.commit()

    def search_by_position(self, position: int) -> List[Tuple]:
        """
        Поиск сотрудников по должности

        :param position: int
        :return: List[Tuple]
        """
        self.cursor.execute(
            'SELECT * FROM employees WHERE position = %s',
            (position,)
        )
        return self.cursor.fetchall()


# Пример использования
if __name__ == '__main__':
    db_handler = ChildDatabaseHandler(
        dbname='postgres',
        user='postgres',
        password='newpassword'
    )

    db_handler.write_csv_db('/home/k/Desktop/practice/Mirbekov_KM/task_4/employees.csv')

    developers = db_handler.search_by_position('разработчик')
    print('Разработчики:', developers)

    db_handler.update_salary_by_name('Иван', 75000)

    db_handler.close()
