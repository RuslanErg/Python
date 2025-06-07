# from lesson_01.lesson_1_task_3 import first_name, last_name
#
#
# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
# print(first_name)
# print(last_name)
# print(first_name + ' ' + last_name)


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_first_name(self):
        print(self.first_name)

    def print_last_name(self):
        print(self.last_name)

    def print_full_name(self):
        print(f"{self.first_name} {self.last_name}")

user = User("Иван", "Петров")
user.print_first_name()
user.print_last_name()
user.print_full_name()  