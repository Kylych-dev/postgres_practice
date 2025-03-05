import psycopg2
import logging
from typing import (
    List,
    Tuple
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseHandler:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.conn.cursor()
        logger.info('Подключение к БД установлено')

    def create_table(self) -> None:
        """
        Создание таблицы employees

        :return: None
        """
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS employees (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    position VARCHAR(100),
                    salary INTEGER
                )
            ''')
        self.conn.commit()
        logger.info('Таблица employees создана')

    def add_employees(self, name: str, position: str, salary: int) -> None:
        """
        Добавление сотрудника в таблицу

        :param name: str
        :param position: str
        :param salary: int
        :return: None
        """

        self.cursor.execute(
            'INSERT INTO employees (name, position, salary) VALUES (%s, %s, %s)',
            (name, position, salary)
        )
        self.conn.commit()
        logger.info(f'Сотрудник {name} добавлен')

    def get_high_salary(self) -> List[Tuple[int, str, str, int]]:
        """
        Получение списка сотрудников с зарплатой выше 50_000

        :return: List[Tuple[int, str, str, int]]
        """
        self.cursor.execute('SELECT * FROM employees WHERE salary > 50000')
        return self.cursor.fetchall()

    def update_salary_by_name(self, name: str, new_salary: int) -> None:
        """
        Обновление зарплаты сотрудника по имени

        :param name: str
        :param new_salary: int
        :return: None
        """

        self.cursor.execute(
            'UPDATE employees SET salary = %s WHERE name = %s',
            (new_salary, name)
        )
        self.conn.commit()
        logger.info(f'Зарплата сотрудника {name} обновлена на {new_salary}')

    def delete_empl_by_name(self, name: str) -> None:
        """
        Удаление сотрудника по имени
        :param name: str
        :return: None
        """
        self.cursor.execute(
            'DELETE FROM employees WHERE name = %s',
            (name,)
        )
        self.conn.commit()
        logger.info(f'Сотрудник {name} удален')

    def close(self) -> None:
        """
        Закрытие соединения с базой данных
        :return: None
        """
        self.cursor.close()
        self.conn.close()
        logger.info('Соединение с базой данных закрыто')


if __name__ == '__main__':
    db_params = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': 'newpassword',
        'host': 'localhost',
        'port': '5432'
    }
    db = DatabaseHandler(**db_params)

    try:
        db.create_table()

        test_employees = [
            ('Иван', 'Разработчик', 55000),
            ('Анна', 'Менеджер', 48000),
            ('Петр', 'Аналитик', 60000),
            ('Мария', 'Дизайнер', 52000),
            ('Сергей', 'Тестировщик', 45000)
        ]

        for emp in test_employees:
            db.add_employees(*emp)

        print('\nСотрудники с зарплатой больше 50000:')
        high_salary = db.get_high_salary()
        for emp in high_salary:
            print(emp)
        print()

        db.update_salary_by_name('Мария', 15000)

        db.delete_empl_by_name('Анна')

    finally:
        db.close()
