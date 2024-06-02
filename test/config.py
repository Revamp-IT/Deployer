# Словарь с параметрами подключения к серверам
servers = {
    "server1": {
        "address": "217.18.63.26",
        "username": "root",
        "password": "w.h-UTn5jgvccE"
    },
    "server2": {
        "address": "192.168.1.2",
        "username": "admin",
        "password": "password2"
    },
    # Другие сервера...
}

# Директории скриптов и файлов
local_scripts = "local_scripts/"  # Директория локальных скриптов
predeploy_scripts = "scripts/"  # Директория скриптов для выполнения на сервере
dist = "input/"  # Директория с файлами для отправки на сервер
dest = "output/"  # Директория для размещения файлов на сервере
postdeploy_scripts = "deploy_scripts/"