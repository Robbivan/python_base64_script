import base64
import sys

def get_base64_from_file(filename):
    try:
        base64_content = base64.b64encode(filename.encode('utf-8')).decode('utf-8')
        return base64_content
    except IOError:
        print("Ошибка: Невозможно прочитать файл.")
        return None

# Проверяем, был ли передан аргумент с именем файла
if len(sys.argv) < 2:
    print("Ошибка: Укажите имя файла в качестве аргумента.")
else:
    filename = sys.argv[1]
    base64_value = get_base64_from_file(filename)
    if base64_value:
        print(base64_value)

