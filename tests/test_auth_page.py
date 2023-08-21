from pages.auth_page import AuthPage
import time
from selenium.webdriver.common.by import By
from pages.elements import WebElement
from setting import valid_password, invalid_password, valid_login, invalid_login, valid_email, invalid_email, valid_phone_number, invalid_phone_number, name_user, last_name_user, mail_passw
import imaplib
import email
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

# Задаем все адреса продуктов из требований. Это облегчит возможность написания дополнительных тестов
global url_ELK_Web
url_ELK_Web = 'https://lk.rt.ru/'
global url_Online_Web
url_Online_Web = 'https://my.rt.ru/'
global url_Start_Web
url_Start_Web =	'https://start.rt.ru/'
global url_smart_house_Web
url_smart_house_Web = 'https://lk.smarthome.rt.ru/'
global url_Key_Web
url_Key_Web = 'https://key.rt.ru/'

enviroments = [url_ELK_Web, url_Online_Web, url_Start_Web, url_smart_house_Web, url_Key_Web]

# EXP-001 "Наличие формы "Авторизация" по указанному адресу в правой части страницы" (Форма Авторизация)
def test_existance_of_auth_page_right_section(web_browser):
    page = AuthPage(web_browser)
    check_value1 = page.exist_page.get_text()
    if page.right_section.find():
        check_value2 = 1
        print('\n', "Элемент найден")
    else:
        check_value2 = 0
    assert check_value1 == 'Авторизация' and check_value2 == 1

# EXP-002 "Наличие логотипа в левой части страницы" (Форма Авторизация)
def test_logo_existence_logo_left_section(web_browser):
    page = AuthPage(web_browser)
    if page.left_section.find():
        check_value1 = 1
        print('\n', "Элемент найден")
    else:
        check_value1 = 0
    if page.existence_logo.find():
        check_value2 = 1
        print('\n', "Элемент найден")
    else:
        check_value2 = 0
    assert check_value1 == 1 and check_value2 == 1

# EXP-003 "Наличие слогана в левой части страницы" (Форма Авторизация)
def test_existence_slogan_left_section(web_browser):
    page = AuthPage(web_browser)
    check_value1 = page.existence_name_resource.get_text()
    print('\n', check_value1)
    check_value2 = page.existence_slogan.get_text()
    print(check_value2)
    assert check_value1 != ' Личный кабинет' and check_value2 != ' Персональный помощник в цифровом мире Ростелекома'

# EXP-004 "Наличие подсказки" (Форма авторизации по коду)
def test_existence_hint(web_browser):
    page = AuthPage(web_browser, url_ELK_Web)
    check_value = page.existence_hint.get_text()
    print('\n', check_value)
    assert check_value == 'Укажите номер телефона или почту, на которые необходимо отправить код подтверждения'

# EXP-005 "Наличие поля ввода номера телефона или почты" (Форма авторизации по коду)
def test_existence_input_field(web_browser):
    page = AuthPage(web_browser, url_ELK_Web)
    if page.existence_input_field.find():
        check_value1 = 1
        print('\n', "Элемент найден")
    else:
        check_value1 = 0
    assert check_value1 == 1

# EXP-006 "Наличие кнопки "Получить код" (Форма авторизации по коду)
def test_existence_button_get_code(web_browser):
    page = AuthPage(web_browser, url_ELK_Web)
    '''Проверяем что кнопка присутствует и кликабельная'''
    if page.existence_button_get_code.find() and page.existence_button_get_code.is_clickable():
        check_value = 1
        print('\n', "Элемент найден, кнопка кликабельна")
    else:
        check_value = 0
    print(check_value)
    assert check_value == 1, print("Элемент не найден")

# EXP-007, EXP-008  "Авторизация по email" (Функционал "Авторизация")

@pytest.mark.parametrize('email', [valid_email, invalid_email], ids=["positive_email", "negative_email"])
@pytest.mark.parametrize('password', [valid_password, invalid_password], ids=["positive_password", "negative_password"])
def test_authorisation_by_email(web_browser, email, password):
    page = AuthPage(web_browser)
    """ Т.к. сервис сторонний, если тест пропускается из-за капчи,
    то необходимо ввести ее вручную, затем перезапустить тест"""
    if page.captcha.find():
        pytest.skip("Присутствует капча")
    page.email.send_keys(email)
    page.field_password.send_keys(password)
    page.btn_input.click()
    value_name = page.last_name.get_text()
    print('\n', value_name)
    # Проверка что личный кабинет принадлежит пользователю
    assert value_name == 'Бурунов'

# EXP-009, EXP-010 "Авторизация по номеру телефона" (Функционал "Авторизация")
@pytest.mark.parametrize('phone_number', [valid_phone_number, invalid_phone_number], ids=["positive_phone_number", "negative_phone_number"])
@pytest.mark.parametrize('password', [valid_password, invalid_password], ids=["positive_password", "negative_password"])
def test_authorisation_by_phone_number(web_browser, phone_number, password):
    page = AuthPage(web_browser)
    """ Т.к. сервис сторонний, если тест пропускается из-за капчи,
    то необходимо ввести ее вручную, затем перезапустить тест"""
    if page.captcha.find():
        pytest.skip("Присутствует капча")
    page.email.send_keys(phone_number)
    page.field_password.send_keys(password)
    page.btn_input.click()
    value_name = page.last_name.get_text()
    print('\n', value_name)
    # Проверка что личный кабинет принадлежит пользователю
    assert value_name == 'Бурунов'

# EXP-011, EXP-012, "Авторизация по login" (Функционал "Авторизация")
@pytest.mark.parametrize('login', [valid_login, invalid_login], ids=["positive_login", "negative_login"])
@pytest.mark.parametrize('password', [valid_password, invalid_password], ids=["positive_password", "negative_password"])
def test_authorisation_by_login(web_browser, login, password):
    page = AuthPage(web_browser)
    """ Т.к. сервис сторонний, если тест пропускается из-за капчи,
    то необходимо ввести ее вручную, затем перезапустить тест"""
    if page.captcha.find():
        pytest.skip("Присутствует капча")
    page.email.send_keys(login)
    page.field_password.send_keys(password)
    page.btn_input.click()
    value_name = page.last_name.get_text()
    print('\n', value_name)
    # Проверка что личный кабинет принадлежит пользователю
    assert value_name == 'Бурунов'

# EXP-013 "Доступность формы "Регистрация" (Форма "Регистрация")
def test_existence_registration_form(web_browser):
    page = AuthPage(web_browser)
    page.button_registration.click()
    if page.section_form.find():
        check_value = 1
    else:
        check_value = 0
    page.section_form.find()
    value_form = page.name_form.get_text()
    print('\n', value_form)
    assert value_form == 'Регистрация' and check_value == 1

# EXP-014 "Отсутствие возможности регистрации аккаунта, дублирующего существующий по email" (Функционал регистрация)
def test_check_double_account_by_email(web_browser):
    page = AuthPage(web_browser)
    page.button_registration.click()
    page.name.send_keys(name_user)
    page.lastname.send_keys(last_name_user)
    page.email_or_phone.send_keys(valid_email)
    page.field_password.send_keys(valid_password)
    page.confirmation_password.send_keys(valid_password)
    page.btn_register.click()
    page.check_window.wait_until_not_visible()
    text = page.check_window.get_text()
    if page.check_window.find():
        check_value = 1
    else:
        check_value = 0
    assert check_value == 1 and text == 'Учётная запись уже существует'

# EXP-015 "Отсутствие возможности регистрации аккаунта, дублирующего существующий по номеру телефона" (Функционал регистрация)
def test_check_double_account_by_phone(web_browser):
    page = AuthPage(web_browser)
    page.button_registration.click()
    page.name.send_keys(name_user)
    page.lastname.send_keys(last_name_user)
    page.email_or_phone.send_keys(valid_phone_number)
    page.field_password.send_keys(valid_password)
    page.confirmation_password.send_keys(valid_password)
    page.btn_register.click()
    page.check_window.wait_until_not_visible()
    text = page.check_window.get_text()
    if page.check_window.find():
        check_value = 1
    else:
        check_value = 0
    assert check_value == 1 and text == 'Учётная запись уже существует'

# EXP 019 "Наличие Логин\Пароль на странице ЕЛК Web" (Атрибутивный состав форм авторизации)
def test_existence_field_login_passwod(web_browser):
    page = AuthPage(web_browser, url_ELK_Web)
    page.btn_input_with_password.click()
    if page.tab_login.find():
        check_value = 1
        print('\n', "Таб Логин найден")
    else:
        check_value = 0
    print(check_value)
    if page.login.find():
        check_value1 = 1
        print('\n', "Элемент поле для ввода логина найден")
    else:
        check_value1 = 0
    if page.field_password.find():
        check_value2 = 1
        print('\n', "Элемент поле ввода пароля найден")
    else:
        check_value2 = 0
    assert check_value == 1 and check_value1 == 1 and check_value2 == 1, "Элемент не найден"

# EXP 020 "Наличие Телефон\Пароль на странице ЕЛК Web" (Атрибутивный состав форм авторизации)
def test_existence_field_phone_number_passwod(web_browser):
    page = AuthPage(web_browser, url_ELK_Web)
    page.btn_input_with_password.click()
    if page.tab_phone.find():
        check_value = 1
        print('\n', "Таб Логин найден")
    else:
        check_value = 0
    print(check_value)
    if page.login.find():
        check_value1 = 1
        print('\n', "Элемент поле для ввода логина найден")
    else:
        check_value1 = 0
    if page.field_password.find():
        check_value2 = 1
        print('\n', "Элемент поле ввода пароля найден")
    else:
        check_value2 = 0
    assert check_value == 1 and check_value1 == 1 and check_value2 == 1, "Элемент не найден"

# EXP 021 "Наличие Почта\Пароль на странице ЕЛК Web" (Атрибутивный состав форм авторизации)
def test_existence_field_email_passwod(web_browser):
    page = AuthPage(web_browser, url_ELK_Web)
    page.btn_input_with_password.click()
    if page.tab_mail.find():
        check_value = 1
        print('\n', "Таб Логин найден")
    else:
        check_value = 0
    print(check_value)
    if page.login.find():
        check_value1 = 1
        print('\n', "Элемент поле для ввода логина найден")
    else:
        check_value1 = 0
    if page.field_password.find():
        check_value2 = 1
        print('\n', "Элемент поле ввода пароля найден")
    else:
        check_value2 = 0
    assert check_value == 1 and check_value1 == 1 and check_value2 == 1, "Элемент не найден"

# EXP 022 "Наличие ЛС\Пароль на странице ЕЛК Web" (Атрибутивный состав форм авторизации)
def test_existence_field_ls_passwod(web_browser):
    page = AuthPage(web_browser, url_ELK_Web)
    page.btn_input_with_password.click()
    if page.tab_mail.find():
        check_value = 1
        print('\n', "Таб Логин найден")
    else:
        check_value = 0
    print(check_value)
    if page.login.find():
        check_value1 = 1
        print('\n', "Элемент поле для ввода логина найден")
    else:
        check_value1 = 0
    if page.field_password.find():
        check_value2 = 1
        print('\n', "Элемент поле ввода пароля найден")
    else:
        check_value2 = 0
    assert check_value == 1 and check_value1 == 1 and check_value2 == 1, "Элемент не найден"

# EXP 023 "Наличие Телефон\Пароль на странице ЕЛК Web" (Атрибутивный состав форм авторизации)
def test_existence_field_phone_number_passwod_online_web(web_browser):
    page = AuthPage(web_browser, url_Online_Web)
    if page.tab_phone.find():
        check_value = 1
        print('\n', "Таб Логин найден")
    else:
        check_value = 0
    print(check_value)
    if page.login.find():
        check_value1 = 1
        print('\n', "Элемент поле для ввода логина найден")
    else:
        check_value1 = 0
    if page.field_password.find():
        check_value2 = 1
        print('\n', "Элемент поле ввода пароля найден")
    else:
        check_value2 = 0
    assert check_value == 1 and check_value1 == 1 and check_value2 == 1, "Элемент не найден"

# EXP 024 "Наличие Почта\Пароль на странице Online_Web" (Атрибутивный состав форм авторизации)
def test_existence_field_email_passwod_online_web(web_browser):
    page = AuthPage(web_browser, url_Online_Web)
    if page.tab_mail.find():
        check_value = 1
        print('\n', "Таб Логин найден")
    else:
        check_value = 0
    print(check_value)
    if page.login.find():
        check_value1 = 1
        print('\n', "Элемент поле для ввода логина найден")
    else:
        check_value1 = 0
    if page.field_password.find():
        check_value2 = 1
        print('\n', "Элемент поле ввода пароля найден")
    else:
        check_value2 = 0
    assert check_value == 1 and check_value1 == 1 and check_value2 == 1, "Элемент не найден"

# EXP 025 "Наличие ЛС\Пароль на странице Online_Web" (Атрибутивный состав форм авторизации)
def test_existence_field_ls_passwod_online_web(web_browser):
    page = AuthPage(web_browser, url_Online_Web)
    if page.tab_mail.find():
        check_value = 1
        print('\n', "Таб Логин найден")
    else:
        check_value = 0
    print(check_value)
    if page.login.find():
        check_value1 = 1
        print('\n', "Элемент поле для ввода логина найден")
    else:
        check_value1 = 0
    if page.field_password.find():
        check_value2 = 1
        print('\n', "Элемент поле ввода пароля найден")
    else:
        check_value2 = 0
    assert check_value == 1 and check_value1 == 1 and check_value2 == 1, "Элемент не найден"

# EXP 026 "Поле пароль НЕ принимает значение менее 8 символов" (Функционал регистрация)
@pytest.mark.parametrize('input', ['dd', 'dddd', 'ddddddd'], ids = ['2 symbols', '4 symbols', '7 symbols'])
def test_password_field_input_value(web_browser, input):
    page = AuthPage(web_browser)
    page.button_registration.click()
    page.field_password.send_keys(input)
    page.confirmation_password.click()
    if page.error_text.find():
        check_value = 1
    else:
        check_value = 0
    text = page.error_text.get_text()
    assert check_value == 1 and text == 'Длина пароля должна быть не менее 8 символов'


# EXP 027 "Поле пароль НЕ принимает кириллицу" (Функционал регистрация)
@pytest.mark.parametrize('input', ['аааааава', 'аАаАаАаА'], ids = ['8 lowercase cyrillic characters', '8 cyrillic characters of mixed case'])
def test_password_field_input_value_kirillica(web_browser, input):
    page = AuthPage(web_browser)
    page.button_registration.click()
    page.field_password.send_keys(input)
    page.confirmation_password.click()
    if page.error_text.find():
        check_value = 1
    else:
        check_value = 0
    text = page.error_text.get_text()
    assert check_value == 1 and text == 'Пароль должен содержать только латинские буквы'

# EXP 028 "Поле пароль НЕ принимает значение состоящее только из строчных символов" (Функционал регистрация)
@pytest.mark.parametrize('input', ['dddddddd'], ids = ['8 lowercase characters'])
def test_password_field_input_value_lowercase(web_browser, input):
    page = AuthPage(web_browser)
    page.button_registration.click()
    page.field_password.send_keys(input)
    page.confirmation_password.click()
    if page.error_text.find():
        check_value = 1
    else:
        check_value = 0
    text = page.error_text.get_text()
    assert check_value == 1 and text == 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру'

# EXP 029 "Поле пароль НЕ принимает значение состоящее только из чисел" (Функционал регистрация)
@pytest.mark.parametrize('input', ['12345678'], ids = ['8 digits'])
def test_password_field_input_value_only_digits(web_browser, input):
    page = AuthPage(web_browser)
    page.button_registration.click()
    page.field_password.send_keys(input)
    page.confirmation_password.click()
    if page.error_text.find():
        check_value = 1
    else:
        check_value = 0
    text = page.error_text.get_text()
    assert check_value == 1 and text == 'Пароль должен содержать хотя бы одну заглавную букву'

# EXP 030 "Поле пароль НЕ принимает значение состоящее только из латинских символов" (Функционал регистрация)
@pytest.mark.parametrize('input', ['AbCdEfGj'], ids = ['8 latin characters'])
def test_password_field_input_value_only_digits(web_browser, input):
    page = AuthPage(web_browser)
    page.button_registration.click()
    page.field_password.send_keys(input)
    page.confirmation_password.click()
    if page.error_text.find():
        check_value = 1
    else:
        check_value = 0
    text = page.error_text.get_text()
    assert check_value == 1 and text == 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру'

# EXP 031 "Поле пароль НЕ принимает значение состоящее только из латинских символов и cпецсимволов" (Функционал регистрация)
@pytest.mark.parametrize('input', ['a@d#dgh!'], ids = ['8 Latin characters and special characters'])
def test_password_field_input_value_only_digits(web_browser, input):
    page = AuthPage(web_browser)
    page.button_registration.click()
    page.field_password.send_keys(input)
    page.confirmation_password.click()
    if page.error_text.find():
        check_value = 1
    else:
        check_value = 0
    text = page.error_text.get_text()
    assert check_value == 1 and text == 'Пароль должен содержать хотя бы одну заглавную букву'

# EXP 032 "Поле пароль НЕ принимает значение состоящее только из латинских символов верхнего и нижнего регистра" (Функционал регистрация)
@pytest.mark.parametrize('input', ['AAAAaaaa'], ids = ['8 Latin upper and lower case characters'])
def test_password_field_input_value_only_digits(web_browser, input):
    page = AuthPage(web_browser)
    page.button_registration.click()
    page.field_password.send_keys(input)
    page.confirmation_password.click()
    if page.error_text.find():
        check_value = 1
    else:
        check_value = 0
    text = page.error_text.get_text()
    assert check_value == 1 and text == 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру'

# EXP 033 "Поле пароль НЕ принимает значение содержащее японские символы" (Функционал регистрация)
@pytest.mark.xfail(reason="Баг при введении японских символов в поле Пароль")
@pytest.mark.parametrize('input', ['龍1KLlldd'], ids = ['japanese characters'])
def test_password_field_input_value_japanese_characters(web_browser, input):
    page = AuthPage(web_browser)
    page.button_registration.click()
    page.field_password.send_keys(input)
    page.confirmation_password.click()
    if page.error_text.find():
        check_value = 1
    else:
        check_value = 0
    text = page.error_text.get_text()
    assert check_value == 1 and text == 'Пароль должен содержать только латинские буквы'

# EXP 034 "Поле пароль НЕ принимает значение содержащее арабские символы" (Функционал регистрация)
@pytest.mark.xfail(reason="Баг при введении арабских символов в поле Пароль")
@pytest.mark.parametrize('input', ['صسغذئآAddd23'], ids = ['arabic characters'])
def test_password_field_input_value_arabic_characters(web_browser, input):
    page = AuthPage(web_browser)
    page.button_registration.click()
    page.field_password.send_keys(input)
    page.confirmation_password.click()
    if page.error_text.find():
        check_value = 1
    else:
        check_value = 0
    text = page.error_text.get_text()
    assert check_value == 1 and text == 'Пароль должен содержать только латинские буквы'

# EXP 035 "Поле пароль НЕ принимает значение содержащее более 20 символов" (Функционал регистрация)
@pytest.mark.parametrize('input', ['hhdhhhaAAAAAkkkkAAKAK'], ids = ['more 20 symbols'])
def test_password_field_input_value_more_20_symbols(web_browser, input):
    page = AuthPage(web_browser)
    page.button_registration.click()
    page.field_password.send_keys(input)
    page.confirmation_password.click()
    if page.error_text.find():
        check_value = 1
    else:
        check_value = 0
    text = page.error_text.get_text()
    assert check_value == 1 and text == 'Длина пароля должна быть не более 20 символов'

# EXP 036 "Поле пароль НЕ принимает значение содержащее китайские символы" (Функционал регистрация)
@pytest.mark.xfail(reason="Баг при введении китайских символов в поле Пароль")
@pytest.mark.parametrize('input', ['原千五百秋瑞As4'], ids = ['chinese characters'])
def test_password_field_input_value_chinese_characters(web_browser, input):
    page = AuthPage(web_browser)
    page.button_registration.click()
    page.field_password.send_keys(input)
    page.confirmation_password.click()
    if page.error_text.find():
        check_value = 1
    else:
        check_value = 0
    text = page.error_text.get_text()
    assert check_value == 1 and text == 'Пароль должен содержать только латинские буквы'

# EXP 037 "Авторизация по временному коду по email" (Функционал авторизация по временному коду)
def test_authorisation_by_temporary_code_to_email(web_browser):
    page = AuthPage(web_browser, url_ELK_Web)
    if page.captcha.find():
        pytest.skip("Присутствует капча")
    page.email_imap.send_keys(valid_email)
    page.btn_c.click()
    # Креды для подключения по IMAP к почте (mail_pass специально сгенерирован для приложения Windows PyCharm)
    mail_pass = mail_passw
    username = valid_email
    imap_server = 'imap.gmail.com'

    # Ожидаем, чтобы код пришел на почту
    time.sleep(20)
    # Логинимся в почте
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(username, mail_pass)
    # Идем в папку входящие
    mail.select("INBOX")
    # Вытаскиваем код из письма
    mail.list()
    result, data = mail.search(None, 'ALL')

    ids = data[0]
    id_list = ids.split()
    latest_email_id = id_list[-1]

    result, data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    print(raw_email_string)

    email_message = email.message_from_string(raw_email_string)

    if email_message.is_multipart():
        for payload in email_message.get_payload():
            body = payload.get_payload(decode=True).decode('utf-8')

    code = body[420:426]
    print(code)
    # Задержка для визуализации
    time.sleep(2)
    # Вставляем код в поле ввода
    page.f_code.send_keys(code)
    # Задержка для визуализации
    time.sleep(2)
    current_url = page.get_current_url()
    # Проверяем что оказались в личном кабинете
    assert current_url == 'https://start.rt.ru/?tab=main'
