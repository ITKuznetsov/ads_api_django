## Основные технологии
* Python
* Django
* Django REST Framework
* PostgreSQL
## Локальный запуск (Linux)
1. Перейдите в директорию приложения, затем создайте и активируйте виртуальное окружение
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Установите зависимости
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. Создайте файл .env и установите необходимые ключи для settings.py и подключения к СУБД PostgreSQL (SECRET_KEY, NAME_DB, USER_DB, PASSWORD_DB)
   ```bash
   touch .env
   ```

4. Создайте и выполните миграции
   ```bash
   python manage.py makemigrations
   ```
   Выполните миграции
   ```bash
   python manage.py migrate
   ```

5. Запустите локальный сервер
   ```bash
   python manage.py runserver
   ```
