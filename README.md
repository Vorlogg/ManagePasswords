# ManagePasswords
Менеджер паролей для хранения в различных паролей в настольном приложении(интерфейс на PyQt5).\
Данные хранятся в зашифровоном виде в базе данных,при первом запуске указывается ключ доступа(хранится отдельно от бд).\
Функционал:
1. Добавление,удаление и редактирование записей
2. Поиск записей
3. Копирование значений из ячейки двоиным кликом
4. Ключ указывается в файле crypto.py\
Рекомендуется скомпилировать из исходников exe(например auto_py_to_exe)