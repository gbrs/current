from memory_profiler import profile


@profile
def my_func():
    def generate_random_list(list_size):
        """
        генерация случайного списка из целых чисел
        :param list_size: размер генерируемого списка
        :return: list int, список из целых чисел
        """
        from random import randint
        range_of_values = list_size // 2
        return [randint(-range_of_values, range_of_values) for i in range(list_size)]


    def generate_step(step):
        """
        генерирует следующее значение шага: в 1.247 раза меньше предыдущего
        :param step: int, предыдущее значение шага
        :return: int, следующее значение шага (округленное вниз)
        """
        next_step = step / 1.247
        return int(next_step)


    def move_bubble_right_by_jump(step):
        """
        гонит пузырьки больших чисел вправо, но не обязательно соседних элементов,
        а отстоящих друг от друга на step, изменяющийся при каждом вызове функции
        :param step: int, шаг, на который отстоят друг от друга обмениваемые элементы
        :return: None
        side effects: сортирует глобальный массив lst
        """
        current_number = 0
        while current_number + step < LIST_SIZE:
            if lst[current_number] > lst[current_number + step]:
                lst[current_number], lst[current_number + step] \
                    = lst[current_number + step], lst[current_number]
            current_number += 1

    LIST_SIZE = 1000
    lst = generate_random_list(LIST_SIZE)
    step = LIST_SIZE - 1
    # print(f'{step: < 4}, {lst}')

    # сортируем сперва с большим шагом, но каждый раз шаг уменьшаем
    while step > 0:
        move_bubble_right_by_jump(step)
        # print(f'{step: < 4}, {lst}')
        step = generate_step(step)

    # print(f'{step: < 4}, {lst}')

if __name__ == '__main__':
    my_func()
