import psycopg2
import logging
from typing import List, Tuple

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProductDatabaseHandler:
    def __init__(self, dbname: str, user: str, password: str, host: str = 'localhost', port: int = 5432):
        """
        Инициализация подключения к базе данных

        :param dbname: Имя базы данных
        :param user: Имя пользователя
        :param password: Пароль
        :param host: Хост
        :param port: Порт
        """
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.conn.cursor()
        logger.info('Подключение к базе данных установлено')

    def create_table(self) -> None:
        """
        Создание таблицы products

        :return: None
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                quantity INT NOT NULL
            )
        ''')
        self.conn.commit()
        logger.info('Таблица products создана')

    def add_product(self, name: str, price: float, quantity: int) -> None:
        """
        Добавление продукта в таблицу

        :param name: Название продукта
        :param price: Цена продукта
        :param quantity: Количество продукта
        :return: None
        """
        self.cursor.execute('''
            INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)
        ''', (name, price, quantity))
        self.conn.commit()
        logger.info(f'Продукт "{name}" добавлен')

    def get_products_with_low_quantity(self) -> List[Tuple[int, str, float, int]]:
        """
        Получение списка продуктов с количеством меньше 10

        :return: List[Tuple[int, str, float, int]]
        """
        self.cursor.execute('SELECT * FROM products WHERE quantity < 10')
        low_quantity_products = self.cursor.fetchall()
        logger.info(f'Найдено {len(low_quantity_products)} продуктов с количеством меньше 10')
        return low_quantity_products

    def update_product_price(self, name: str, new_price: float) -> None:
        """
        Обновление цены продукта по имени

        :param name: Название продукта
        :param new_price: Новая цена
        :return: None
        """
        self.cursor.execute('''
            UPDATE products SET price = %s WHERE name = %s
        ''', (new_price, name))
        self.conn.commit()
        logger.info(f'Цена продукта "{name}" обновлена на {new_price}')

    def close(self) -> None:
        """
        Закрытие соединения с базой данных

        :return: None
        """
        self.cursor.close()
        self.conn.close()
        logger.info('Соединение с базой данных закрыто')

# Пример использования
if __name__ == '__main__':
    db_params = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': 'newpassword',
        'host': 'localhost',
        'port': 5432
    }

    db = ProductDatabaseHandler(**db_params)
    try:
        db.create_table()

        test_products = [
            ('Product 1', 10.99, 15),
            ('Product 2', 5.49, 25),
            ('Product 3', 8.99, 5),
            ('Product 4', 14.99, 0),
            ('Product 5', 20.99, 8),
            ('Product 6', 12.99, 18),
            ('Product 7', 7.49, 30),
            ('Product 8', 11.99, 50),
            ('Product 9', 9.99, 7),
            ('Product 10', 6.49, 12)
        ]

        for product in test_products:
            db.add_product(*product)

        low_quantity_products = db.get_products_with_low_quantity()
        print('Продукты с количеством меньше 10:')
        for product in low_quantity_products:
            print(product)

        db.update_product_price('Product 1', 15.99)

        updated_products = db.get_products_with_low_quantity()
        print('\nОбновленные продукты с количеством меньше 10:')
        for product in updated_products:
            print(product)

    finally:
        # Закрываем соединение с базой данных
        db.close()
