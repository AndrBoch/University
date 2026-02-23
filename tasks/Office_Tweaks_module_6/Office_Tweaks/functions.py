import os

class Func:
    def menu(self):
        print(f"Текущий каталог: {os.getcwd()}")
        print("\n")
        print("Выберите действие:")
        print("\n")
        print("0. Сменить рабочий каталог")
        print("1. Преобразовать PDF В Docx")
        print("2. Преобразовать Docx в PDF")
        print("3. Произвести сжатие изображения")
        print("4. Удалить группу файлов")
        print("5. Выход")

    def menu_4(self):
        print("Введите действие: ")
        print("\n")
        print("1. Удалить все файлы начинающиеся на опредлеленную подстроку")
        print("2. Удалить все файлы заканчивающиеся на определенную подстроку")
        print("3. Удалить все файлы содержащие определенную строку")
        print("4. Удалить все файлы по расширению")

    def del_case_1(self, prefix):
        for filename in os.listdir(os.getcwd()):
            if filename.startswith(prefix):
                os.remove(filename)
                print(f"Файл: '{filename}' успешно удален!")

    def del_case_2(self,prefix):
        for filename in os.scandir(os.getcwd()):
            namef, _ = os.path.splitext(filename.name)
            if namef.endswith(prefix):
                os.remove(filename)
                print(f"Файл: '{filename}' успешно удален!")

    def del_case_3(self, prefix):
        for filename in os.listdir(os.getcwd()):
            if prefix in filename:
                os.remove(filename)
                print(f"Файл: '{filename}' успешно удален!")

    def del_case_4(self, prefix):
        for filename in os.listdir(os.getcwd()):
            if filename.lower().endswith(prefix):
                os.remove(filename)
                print(f"Файл: '{filename}' успешно удален!")