from Class import WORKER # Импортируем класс из соседнего файла.


def GetAllMethods():
    Methods = ["1) Добавить сотрудника", "2) Узнать сколько сотрудников работают от стажа", "3) Узнать данные сотрудника","4) Редактировать" ,"5) Завершить программу"];
    return Methods;

def main():
    staff_list = []  # Массив для хранения списка сотрудников.

    while True:
        text = "Какую операцию желаете выполнить? Напишите цифрой. Список операций:"
        methods_list = GetAllMethods()
        text = text + "\n" + "\n".join(methods_list) + "\n";
        try:
            ans = int(input(text))
        except ValueError:
            print("Ошибка: введите целое число.")
            continue

        if ans == 1:
            # Ввод данных
            print("\nВвод данных для сотрудника:")
            try:
                name = input("Фамилия и инициалы: ")
                pos = input("Должность: ")
                sal = float(input("Зарплата: "))
                year = int(input("Год поступления на работу: "))
            except ValueError:
                print("При вводе последних данных была нарушена валидация.")
                continue

            # Создаем объект и добавляем в массив.
            worker = WORKER(name, pos, sal, year)
            staff_list.append(worker)

        elif ans == 2:
            # Логика фильтрации
            threshold = int(input("\nВведите минимальный стаж для поиска: "))

            found = False
            print(f"\nСотрудники со стажем более {threshold} лет:")

            for worker in staff_list:
                if worker.get_experience() > threshold:
                    print(worker.full_name)
                    found = True

            if not found:
                print("Таких работников нет.")
        elif ans == 3:
            if len(staff_list) == 0:
                print("Еще не занесен ни один сотрудник")
                continue

            try:
                choice = int(input("Данные какого сотрудника вы хотите узнать? Укажите цифрой."))
            except ValueError:
                print("Произошла ошибка валидации данных.")
                continue
            if choice > len(staff_list):
                print("Указанного сотрудника нет в перечислении.")
                continue

            staff_choice = staff_list[choice - 1]
            staff_choice.display()
        elif ans == 4:
            if not staff_list:
                print("Список пуст.")
                continue
            try:
                choice = int(input("Номер сотрудника для редактирования: "))
                if 1 <= choice <= len(staff_list):
                    print("Введите новые данные (или старые, если нет изменений):")
                    name = input("Новое ФИО: ")
                    pos = input("Новая должность: ")
                    sal = float(input("Новая зарплата: "))
                    year = int(input("Новый год: "))

                    staff_list[choice - 1].update_data(name, pos, sal, year)
                    print("Данные обновлены.")
                else:
                    print("Неверный номер.")
            except ValueError:
                print("Ошибка валидации при редактировании.")
        elif ans == 5:
            print("Завершить программу...")
            break
        else:
            print("Команда не опознана.")



if __name__ == "__main__":
    main()