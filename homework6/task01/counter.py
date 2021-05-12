"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""

set_of_exceptions = set()  # global variable, which contains objects after resetting


def instances_counter(cls):
    """Some code"""

    class MyUser(cls):
        global set_of_exceptions

        def get_created_instances(self):
            counter = 0
            for name, obj in globals().items():
                if isinstance(obj, User) and obj not in set_of_exceptions:
                    counter += 1
            return counter

        def reset_instances_counter(self):
            counter = 0
            for name, obj in globals().items():
                if isinstance(obj, User):
                    set_of_exceptions.add(obj)
                    counter += 1
            return counter

    return MyUser


@instances_counter
class User:
    pass


if __name__ == "__main__":

    # user.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
