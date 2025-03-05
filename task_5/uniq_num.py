from typing import List

def find_num(numbers: List[int]) -> str:
    """
    Обрабатывает список чисел и выполняет следующие операции:

    1. Определяет количество уникальных чисел в списке.
    2. Находит второе по величине число в списке.
    3. Возвращает список чисел, которые делятся на 3 без остатка.

    :param numbers: List[int]
    :return: str
    """
    # кол-во уникальных чисел
    unique_numbers = set(numbers)
    unique_count = len(unique_numbers)

    # второй по величине число
    first = second = None
    for num in unique_numbers:
        if first is None:
            first = num
        elif num > first:
            second = first
            first = num
        elif second is None or num > second:
            second = num
    sec_large = second if len(unique_numbers) >= 2 else None

    # числа, делящиеся на 3
    div_num = (x for x in numbers if x % 3 == 0)

    div_num_list = list(div_num)

    result = (
        f'Уникальные числа: {unique_count}\n'
        f'Второе по величине число: {sec_large}\n'
        f'Числа, делящиеся на 3: {div_num_list}'
    )

    return result

if __name__ == '__main__':
    input_list = [10, 20, 30, 40, 50, 30, 20, 20, 78]
    print(find_num(input_list))
