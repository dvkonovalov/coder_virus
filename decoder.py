import os
import tkinter as tk
import pyAesCrypt
import getpass


# Функция расшифровки
def decrypt(file, password):
    buffer_size = 64 * 1024
    pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, buffer_size)
    os.remove(file)

# Обход каталогов
def walk(directory, password):
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if ".aes" not in path:
            continue
        if os.path.isfile(path):
            try:
                decrypt(path, password)
            except:
                continue
        else:
            walk(path, password)

def decode():
    password = entry.get()
    path = os.path.join("C:", "Users", getpass.getuser(), "Documents")
    walk(path, password)
    inf_label = tk.Label(root, text="Программа закончила работу", font=("Arial", 14))
    inf_label.pack()


# Создаем графический интерфейс
root = tk.Tk()
root.title("Расшифровака данных")
root.geometry("600x200")  # Set fixed window size

min_label = tk.Label(root, text="Пароль (У вас есть только одна попытка):", font=("Arial", 14))
min_label.pack()

# Создаем виджет для ввода пароля
entry = tk.Entry(root, show="*", font=("Arial", 14))
entry.pack(pady=10)

# Создаем кнопку для проверки пароля
check_button = tk.Button(root, text="Расшифровать", command=decode, font=("Arial", 14))
check_button.pack(pady=5)

# Метка для вывода результата проверки
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()