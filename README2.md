Репозиторий содержит решение задания №2, включающее тест-кейсы и автоматизированные тесты, а также Postman-коллекцию.
Что внутри
- TESTCASES.md — список тест-кейсов
- tests/test_api.py — автотесты (pytest + requests)
- BUGS.md — найденные дефекты
- postman_collection.json — ссылка на оригинальную коллекцию Avito + инструкция по импорту
- requirements.txt
Как запустить
1. Клонируй репозиторий
2. Создай виртуальное окружение:
python3 -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows
3. Установите зависимости:
После активации виртуального окружения установите все необходимые библиотеки:
pip install -r requirements.txt
4. Запустите тесты:
После установки зависимостей, чтобы запустить тесты, выполните:
pytest -v
