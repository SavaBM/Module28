# Final_project
Данные тесты проверяют объект тестирования https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=fe5147cd-4b75-4b4b-bb2a-c4f3e0b3b139&theme&auth_type

Настройка проекта:

1. Создаем виртуальное окружение командой:
    python -m venv venv
2. Активируем виртуальное окружение командой (MacOS/Linux):
    source venv/bin/activate
   для Windows другая команда:
    \env\Scripts\activate.bat
3. Установка зависимостей:
    pip install -r requirements.txt
4. Настроить в IDE(Pycharm) текущий интерпритатор, выбрав текущее виртуальное окружение
   
Запуск тестов:

1. Копируем репозиторий на компьютер
2. Открываем проект в PyCharm
3. Нажмите на зеленую стрелочку слева от названия теста, если она вдруг не появилась, значит вы не установили библиотеку pytest.
   Установите командой: pip install pytest.
4. Для визуализации тестов (включение UI) необходимо выключить режим headless в файле conftest.
