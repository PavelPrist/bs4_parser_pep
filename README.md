### Проект парсинга документации Python и PEP

### Описание:
Парсер собирает информацию о документациях Python и PEP статусах и количество статусов, 
выводит информацию несколькими способами.

Список сайтов для парсинга:

- https://docs.python.org/3/

- https://peps.python.org/

### Шаги для запуска:
**Клонируйте репозиторий:**
```
git@github.com:PavelPrist/bs4_parser_pep.git
```

**Установите и активируйте виртуальное окружение:**
для MacOS:
```
python3 -m venv venv
```

для Windows:
```
python -m venv venv
source venv/bin/activate
source venv/Scripts/activate
```
**Установите зависимости из файла requirements.txt:**
```
pip install -r requirements.txt
```

**Перейдите в папку "src":**
```
cd src/
```

**Запустите парсер в одном из режимов:**

```
python main.py <parser_mode> <args>
```

### Режимы парсера:
При запуске парсера необходимо выбрать один из режимов <parser_mode>:

+ **whats-new**

Парсинг последних обновлений с сайта
```
python main.py whats-new <args>
```

+ **latest-versions**

Парсинг последних версий документации
```
python main.py latest_versions <args>
```

+ **download**

Загрузка и сохранение архива с документацией
```
python main.py download <args>
```

+ **pep**

Парсинг статусов PEP
```
python main.py pep <args>
```

### Аргументы парсера:
**При запуске парсера можно указать дополнительные аргументы <args>:**

+ **Вывести информацию о парсере:**
```
python main.py <parser_mode> -h
python main.py <parser_mode> --help
```

+ **Очистить кеш:**
```
python main.py <parser_mode> -c
python main.py <parser_mode> --clear-cache
```

+ **Настроить режим отображения результатов:**

Сохранение результатов в CSV файл:
```
python main.py <parser_mode> --output file
```
Отображение результатов в табличном формате в консоли:
```
python main.py <parser_mode> --output pretty
```

Если не указывать аргумент --output, результат парсинга будет выведен в консоль:
  
(кроме парсера download)
```
python main.py <parser_mode>
```

**Технологии:**
- Python 3.9
- BeautifulSoup4

### Авторы проекта:# Павел Сердюков, Яндекс-Практикум.
