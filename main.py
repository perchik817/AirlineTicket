class TicketApplication:
    def __init__(self, destination, flight_number, passenger_name, departure_date):
        self.destination = destination
        self.flight_number = flight_number
        self.passenger_name = passenger_name
        self.departure_date = departure_date
        self.left = None
        self.right = None


class TicketApplicationManager:
    def __init__(self):
        self.root = None

    def add_application(self, application):
        if self.root is None:
            self.root = application
        else:
            self._add_application(self.root, application)

    def _add_application(self, node, application):
        if application.flight_number < node.flight_number:
            if node.left is None:
                node.left = application
            else:
                self._add_application(node.left, application)
        else:
            if node.right is None:
                node.right = application
            else:
                self._add_application(node.right, application)

    def delete_application(self, flight_number, departure_date):
        self.root = self._delete_application(self.root, flight_number, departure_date)

    def _delete_application(self, node, flight_number, departure_date):
        if node is None:
            return node

        if flight_number < node.flight_number:
            node.left = self._delete_application(node.left, flight_number, departure_date)
        elif flight_number > node.flight_number:
            node.right = self._delete_application(node.right, flight_number, departure_date)
        else:
            if departure_date < node.departure_date:
                node.left = self._delete_application(node.left, flight_number, departure_date)
            elif departure_date > node.departure_date:
                node.right = self._delete_application(node.right, flight_number, departure_date)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    temp = self._find_minimum(node.right)
                    node.destination = temp.destination
                    node.flight_number = temp.flight_number
                    node.passenger_name = temp.passenger_name
                    node.departure_date = temp.departure_date
                    node.right = self._delete_application(node.right, temp.flight_number, temp.departure_date)
        return node

    def _find_minimum(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search_application(self, flight_number, departure_date):
        return self._search_application(self.root, flight_number, departure_date)

    def _search_application(self, node, flight_number, departure_date):
        if node is None or (node.flight_number == flight_number and node.departure_date == departure_date):
            return node
        if flight_number < node.flight_number:
            return self._search_application(node.left, flight_number, departure_date)
        elif flight_number > node.flight_number:
            return self._search_application(node.right, flight_number, departure_date)

    def display_applications(self):
        self._display_applications(self.root)

    def _display_applications(self, node):
        if node is not None:
            self._display_applications(node.left)
            print("Место назначения:", node.destination)
            print("Номер рейса:", node.flight_number)
            print("Имя пассажира:", node.passenger_name)
            print("Дата вылета:", node.departure_date)
            print("----------------------")
            self._display_applications(node.right)

    def save_applications(self, filename):
        with open(filename, "w") as file:
            self._save_applications(self.root, file)

    def _save_applications(self, node, file):
        if node is not None:
            self._save_applications(node.left, file)
            file.write("Место назначения: " + node.destination + "\n")
            file.write("Номер рейса: " + str(node.flight_number) + "\n")
            file.write("Имя пассажира: " + node.passenger_name + "\n")
            file.write("Дата вылета: " + str(node.departure_date) + "\n")
            file.write("----------------------\n")
            self._save_applications(node.right, file)
    @staticmethod
    def display_menu():
        print("========== Система подачи заявок на авиабилеты ==========")
        print("1. Добавить заявку на получение билета")
        print("2. Удалить заявку на получение билета")
        print("3. Поиск заявки на билет")
        print("4. Отобразить все заявки")
        print("5. Сохранить заявки в файл")
        print("6. Выход")
        print("=======================================================")
    @staticmethod
    def get_ticket_application_input():
        destination = input("Место назначения: ")
        flight_number = input("Номер рейса: ")
        passenger_name = input("Имя пассажира: ")
        departure_date = input("Дата вылета: ")
        return TicketApplication(destination, int(flight_number), passenger_name, departure_date)

    def handle_choice(choice):
        if choice == 1:
            application = TicketApplicationManager.get_ticket_application_input()
            manager.add_application(application)
            print("Заявка на получение билета успешно добавлена.")
        elif choice == 2:
            flight_number = input("Номер рейса: ")
            departure_date = input("Дата вылета: ")
            manager.delete_application(int(flight_number), departure_date)
            print("Заявка на получение билета успешно удалена.")
        elif choice == 3:
            flight_number = input("Номер рейса: ")
            departure_date = input("Дата вылета: ")
            application = manager.search_application(int(flight_number), departure_date)
            if application:
                print("Заявка на билет:")
                print("Место назначения:", application.destination)
                print("Номер рейса:", application.flight_number)
                print("Имя пассажира:", application.passenger_name)
                print("Дата вылета:", application.departure_date)
            else:
                print("Заявка на билет не найдена.")
        elif choice == 4:
            print("Все заявки:")
            manager.display_applications()
        elif choice == 5:
            filename = "ticket_applications.txt" #input("Enter filename to save applications: ")
            manager.save_applications(filename)
            print("Заявки успешно добавлены в файл ticket_applications.txt.")
        elif choice == 6:
            exit()
        else:
            print("Некорректный выбор. Пожалуйста повторите запрос.")

manager = TicketApplicationManager()

while True:
    TicketApplicationManager.display_menu()
    choice = input("Введите ваш выбор (1-6): ")
    try:
        choice = int(choice)
        TicketApplicationManager.handle_choice(choice = choice)
    except ValueError:
        print("Некорректный выбор. Пожалуйста введите число.")