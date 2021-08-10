# class MyClass:
#     def __init__(self, param_1, param_2):
#         self.param_1 = param_1
#         self.param_2 = param_2
#
#     @property
#     def my_method(self):
#         return f"Параметры, переданные в класс:" \
#                f" {self.param_1} , {self.param_2} "
#
#
# mc = MyClass("text_1", "text_2")
# print(mc.param_1)
# print(mc.param_2)
# print(mc.my_method)


# def decorator_with_args(name):
#     print('> decorator_with_args:', name)
#     def real_decorator(func):
#         print('>> сам декоратор', func.__name__)
#         def decorated(*args, **kwargs):
#             print('>>> перед функцие', func.__name__)
#             ret = func(*args, **kwargs)
#             print('>>> после функции', func.__name__)
#             return ret
#         return decorated
#     return real_decorator
#
# @decorator_with_args('test')
# def add(a, b):
#     print('>>>> функция add')
#     return a + b
#
# print('старт программы')
# r = add(10, 10)
# print(r)
# print('конец программы')


# def decorator(func):
#     '''Декоратор'''
#     def decorated():
#         '''Функция Decorated444'''
#         func()
#     return decorated
#
# @decorator
# def wrapped():
#     '''Оборачиваемая функция'''
#     print('функция wrapped')
#
# print('старт программы...')
# print(wrapped.__name__)
# print(wrapped.__doc__)
# print('конец программы')

# import logging
#
# def logger(func):
#     log = logging.getLogger(__name__)
#     def wrapper(a, b):
#         log.info("Вызов функции ", func.__name__)
#         ret = func(a, b)
#         log.info("Вызвана функция ", func.__name__)
#         return ret
#     return wrapper
#
# @logger
# def add(a, b):
#     print('a + b:', a + b)
#     return a + b
#
# print('>> старт')
# add(10, 20)
# add(20, 30)
#
# print('>> конец')

# user_permissions = ["user", 'admin']


#
#
# def check_permission(permission):
#     print(permission)
#
#     def wrapper_permission(func):
#         def wrapped_check():
#             if permission not in user_permissions:
#                 raise ValueError("Недостаточно прав")
#                 exit()
#             func()
#
#         return wrapped_check
#
#     return wrapper_permission
#
#
# @check_permission("user")
# def check_value():
#     print(123)
#     return "значение"
#
#
# @check_permission("admin")
# def do_something():
#     print('o-lo-lo')
#     return "только админ"
#
#
# print('старт программы')
# check_value()
# do_something()
# print('конец программы')

class Auto:
    # конструктор класса Auto
    def __init__(self, year):
        # Инициализация свойств.
        self.year = year

    # создаем свойство года

    @property
    def year(self):
        return self._year

    # сеттер для создания свойств

    @year.setter
    def year(self, year):
        if year < 2000:
            self._year = 2000
        elif year > 2019:
            self._year = 2019
        else:
            self._year = year

    def get_auto_year(self):
        return f"Автомобиль выпущен в {str(self.year)} году"

print('start')
a = Auto(2090)
print(a.get_auto_year())

input()


# class Student():
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#         self._full_id = self.name + " - " + str(self.id)
#         print('j,]trn cjplfy')
#
#     def get_name(self):
#         return self.name
#
#     @property
#     def full_id(self):
#         print('qw')
#         return self._full_id
#
#     @full_id.setter
#     def full_id(self, value):
#         self._full_id = value
#
#
# s = Student("Amit", 10)
# print(s.name)
# print(s.full_id)
# s.name = "Rahul"
# print(s.name)
# print(s.full_id)
# s.full_id = "Kishore - 20"
# print(s.name)
# print(s.id)
# print(s.full_id)
