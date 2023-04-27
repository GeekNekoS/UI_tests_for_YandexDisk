# UI_tests_for_YandexDisk
Тестирование работы с файлами на YandexDisk через UI
<br /> <br />

## Загрузка и настройка готового проекта
• Версия Python: 3.10

• После скачивания проекта к себе на компьютер не забудьте установить необходимые зависимости, прописав к консоли команду: 
<code>pip install requirements.txt</code>

• Перед запуском теста test_copying_file.py необходимо: 
1) Cоздать файл "Файл для копирования.docx" в общей дерриктории Yandex диска
2) Cоздать папку "Скопировать файл сюда!" в общей дерриктории Yandex диска
3) Cоздать несколько файлов в папке "Скопировать файл сюда!" с любым названием и расширением, короме названия "Файл для копипрования" и расширения docx

• Для корректной работы автотеста test_with_a_mark.py необходимо:
1) Переключиться на английскую раскладку
2) Сделать так, чтобы все окна, кроме открытого браузера с автотестом были свёрнуты 

Это требуется для корректного ввода полного пути до файла для загрузки его в необходимую папку

• Для корректной работы автотестов не забудьте создать файл ".env", куда поместите свои логин и пароль. Если хотите скрыть свои личные данные, помещайти их в файл ".env", в ином случае, можете задать переменные в файле settings.py, а затем импортировать данный файл в файл, в котором собираетесь использовать необходимые переменные
<br /> <br />

## Описание тестк-кейса для теста в файле test_copying_file.py
Предусловие:
1) Открыть браузер

Шаги:
1) Открыть страницу http://yandex.ru
2) Авторизоваться
3) Открыть Яндекс.Диск
4) Скопировать файл “Файл для копирования” в созданную ранее папку
5) Открыть папку
6) Удалить файлы кроме скопированного

Ожидаемый результат:
1) Скопированный файл находится в папке
2) Название соответствует оригиналу

Постусловие:
1) Разлогиниться
2) Закрыть браузер
<br /> <br />

## Описание тестк-кейса для теста в файле test_with_a_mark.py
Предусловие:
1) Открыть браузер

Шаги:
1) Открыть страницу http://yandex.ru
2) Авторизоваться
3) Открыть Яндекс.Диск
4) Создать новую папку и назвать её
5) Открыть папку
6) Загрузить файл расширения .txt с текстом
7) Открыть файл
8) Проверить текст в файле

Ожидаемый результат:
1) Текст соответствует ожиданиям

Постусловие:
1) Разлогиниться
2) Закрыть браузе
<br /> <br />

## Работа с командами, запуск автотестов через консоль
• Для запуска всех существующих тестов в проекте: <code>pytest</code>

• Пример запуска конкретного теста: <code>pytest tests/test_with_a_mark.py</code>
<br /> <br />

## Начало работы над проектом, структура проекта
Проект будет реализован с использование паттерна написания автотестов Page Object Model (POM) для упрощения работы с методами, используемыми в тест-кейсах. Для этого создадим файлы: 

• Base_Page.py, где в классе BaseClass будут описаны неизменяемые методы для работы с Webdriver; 

• Page_Object.py, где будут находиться классы, каждый из которых будет отвечать за методы, работающие с одной конкретной страницей, и назван соответствующе данной странице; 

• Далее создадим папку Tests, в которой реализуем тесты, оописанные бизнес-логикой тетст-кейсов; 

• Также для инициализации Webdriver необходимо создать файл conftest.py (который будет связан с файлом Base_Page.py), где будет находиться функция driver() с Chrome Webdriver, далее будет предусловие авторизации, затем в конструкции yield будут прогоняться автотесты, и далее будут активированы постусловия;

• Для отслеживания потенциальных ошибок, в проекте будет присутствовать технология логирования. Чтобы логи можно было видеть в удобном формате в реальном времени после запуска тестов, создадим специальный файл с настройками логирования - pytest.ini
<br /> <br />

<!-- 
Понравилось:

□ подробный readme

□ есть логгер

□ классный My_file.txt 😀

□ обертки с явными ожиданиями на методы поиска

Места над которыми нужно поработать:
✔️ В предусловиях явно прописано, что необходимо создать аккаунт, предоставить доступ, создать заранее необходимые папки, для того чтобы просто запустить тесты и они прошли. Из-за не выполнения данного условия не могу проверить работоспособность тестов [бред какой-то]

✔️ Есть зададки POM модели, но все равно получается что в Base_Page лежат методы поиска и перехода, а вся остальная куча методов для всех станиц - просто лежит в Page_Object. Надо было сделать разделение на main_page, login_page, disk_page - тогда бы это был полноценный Page_Object

□ В фикстуре инициализации браузера - лежит логика авторизации на странице. Авторизацию лучше было бы вынести в отдельную фикстуру. Что если нам надо протестить страницу авторизации - создавать отдельную фикстуру инициализации бразуера для этого? [исправить]
-->
