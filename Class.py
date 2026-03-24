import datetime

class WORKER:
    def __init__(self, full_name=None, position=None, salary=0, year_joined=None):
        self.full_name = full_name or "Не указано"
        self.position = position or "Стажер"
        self.salary = salary
        self.year_joined = year_joined or datetime.date.today().year

    def __del__(self):
        pass

    def update_data(self, name=None, pos=None, sal=None, year=None):
        if name: self.full_name = name
        if pos: self.position = pos
        if sal: self.salary = sal
        if year: self.year_joined = year

    def display(self):

        print(f"Сотрудник: {self.full_name} | Должность: {self.position} "
              f"| Зарплата: {self.salary} | Год: {self.year_joined}")

    def get_experience(self):
        current_year = datetime.date.today().year
        return current_year - self.year_joined
