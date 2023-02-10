import requests

try:
    checking = requests.get('url', timeout=1)  # Вместо url подставить нужный адрес url
    if checking.status_code == 500:
        print('False')
    else:
        print("True")
except requests.Timeout as err:
    print("False")

# Скрипт проверяет доступность url на статус ответа 500 и timeout
