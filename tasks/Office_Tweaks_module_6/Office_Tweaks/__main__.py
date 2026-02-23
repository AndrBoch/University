from .file_tranformation import Transformation
from .image_compression import ImageCompressor
from .functions import Func
import os


def main():
   flag = True
   transform = Transformation()
   image_comp = ImageCompressor()
   func = Func()
   while (flag):
        func.menu()
        choise = int(input("Ваш выбор: "))
        match choise:
            case 0:
                path = input("Укажите корректный путь к рабочему каталогу: ")
                try:
                    os.chdir(path)
                except:
                    print("Неверный путь!")

            case 1:
                folder = os.getcwd()
                files = [f.name for f in os.scandir(folder) if f.name.lower().endswith(".pdf")]
                print("Список файлов с расширением .pdf в данном каталоге: ")
                counter = 1
                for i in files:
                    print(f"{counter}. {i}") 
                    counter+=1
                choiseFile = int(input("Введите номер файла для преобразования (Чтобы преобразовать все файлы из данного каталога введите 0): "))
                if choiseFile != 0: 
                    try:
                        transform.pdf_to_docx(files[choiseFile-1])
                    except:
                        print("Такого файла нет в данной папке!")
                else:
                    for i in files:
                        transform.pdf_to_docx(i)

            case 2:
                folder = os.getcwd()
                files = [f.name for f in os.scandir(folder) if f.name.lower().endswith(".docx")]
                print("Список файлов с расширением .docx в данном каталоге: ")
                counter = 1
                for i in files:
                    print(f"{counter}. {i}") 
                    counter+=1
                choiseFile = int(input("Введите номер файла для преобразования (Чтобы преобразовать все файлы из данного каталога введите 0): "))
                if choiseFile != 0: 
                    try:
                        transform.docx_to_pdf(files[choiseFile-1])
                    except:
                        print("Такого файла нет в данной папке!")
                else:
                    for i in files:
                        transform.docx_to_pdf(i)

            case 3:
                folder = os.getcwd()
                files = [f.name for f in os.scandir(folder) if f.name.lower().endswith(".jpeg") or f.name.lower().endswith(".jpg") or f.name.lower().endswith(".png") or f.name.lower().endswith(".gif")]
                print("Список файлов с расширением ('.jpeg', '.jpg', '.png', '.gif') в данном каталоге: ")
                counter = 1
                for i in files:
                    print(f"{counter}. {i}") 
                    counter+=1
                choiseFile = int(input("Введите номер файла для преобразования (Чтобы преобразовать все файлы из данного каталога введите 0): "))
                quality = int(input("Введите параметры сжатия (от 0 до 100%):"))
                if choiseFile != 0:
                    try:
                        image_comp.compression(files[choiseFile-1], quality)
                    except:
                        print("Такого файла нет в данной папке!")
                else:
                    for i in files:
                        image_comp.compression(i, quality)

            case 4:
                func.menu_4()
                choiseF = int(input("Введите номер действия: "))
                match choiseF:
                    case 1:
                        pr = input("Введите подстроку: ")
                        func.del_case_1(pr)

                    case 2:
                        pr = input("Введите подстроку: ")
                        func.del_case_2(pr)

                    case 3:
                        pr = input("Введите подстроку: ")
                        func.del_case_3(pr)

                    case 4:
                        pr = input("Введите расширение: ")
                        func.del_case_4(pr)

            case 5:
                flag = False

            case _:
                print("Введено неверное значение!")
if __name__ == "__main__":
    main()