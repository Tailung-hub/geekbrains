"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position  реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self):
        name = "Петр"
        surname = "Куликов"
        position = "Старший инженер"
        _income = {"Оклад": 30000, "Премия": 10000}


class Position(Worker):
    def get_full_name(self):
        print("Полное имя: ", Worker.name, Worker.surname)

    def get_total_income(self):
        print("Полный доход: ", Worker._income.get("Оклад") + Worker._income.get("Премия"))


p = Position()
p.get_full_name()
p.get_total_income()
