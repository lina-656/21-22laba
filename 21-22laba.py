from task1 import task1
from task2 import task2
from task3 import task3
from concurrent.futures import ThreadPoolExecutor

def print_menu():
    """Выводит меню с доступными заданиями."""
    print("\nМеню:")
    print("1. Задание 1")
    print("2. Задание 2")
    print("3. Задание 3")
    print("4. Завершение работы программы")

def main():
    """Основная функция программы, которая управляет выбором задания пользователем."""
    with ThreadPoolExecutor() as executor:
        while True:
            print_menu()  # Выводим меню
            choice = input("Выберите пункт меню: ")  # Запрашиваем выбор пользователя

            if choice == '1':
                executor.submit(task1)  # Запускаем задание 1 в фоновом режиме
                executor.join()
            elif choice == '2':
                executor.submit(task2)  # Запускаем задание 2 в фоновом режиме
                executor.join()
            elif choice == '3':
                executor.submit(task3)  # Запускаем задание 3 в фоновом режиме
                executor.join()
            elif choice == '4':
                print("Завершение работы программы.")  # Сообщаем о завершении
                executor.join()
                break  # Выходим из цикла

            else:
                print("Неверный выбор.")  # Обработка неверного выбора

if __name__ == "__main__":
    main()  # Запуск основной функции при выполнении скрипта
