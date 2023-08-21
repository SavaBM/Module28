from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = url if url else 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope=openid&state=45c2c21d-182e-496b-8e97-89dcf817f63a&theme=light&auth_type'
        super().__init__(web_driver, url)

# Указываю локаторы по мере их появления в тестах
    # EXP-001
    right_section = WebElement(id = 'page-right')
    exist_page = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/h1[1]')

    # EXP-002
    existence_logo = WebElement(class_name='rt-logo')
    left_section = WebElement(id='page-left')

    # EXP-003
    existence_name_resource = WebElement(class_name='what-is__title')
    existence_slogan = WebElement(class_name='what-is__desc')

    # EXP - 004
    existence_hint = WebElement(xpath='//*[@id="page-right"]/div/div/p')

    # EXP - 005
    existence_input_field = WebElement(class_name='rt-input__input')

    # EXP - 006
    existence_button_get_code = WebElement(id='otp_get_code')

    # EXP - 007
    btn_input = WebElement(id='kc-login')
    captcha = WebElement(xpath='//*[@id="captcha"]')
    last_name = WebElement(class_name='user-name__last-name')  # Фамилия в личном кабинете после авторизации
    email = WebElement(id='username')
    field_password = WebElement(id='password')

    # EXP - 013
    button_registration = WebElement(xpath='// *[ @ id = "kc-register"]')
    name_form = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/h1[1]')
    section_form = WebElement(xpath='//*[@id="page-right"]')

    # EXP - 014
    name = WebElement(name='firstName')
    lastname = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input')
    region = WebElement(autocomplete='new-password')
    email_or_phone = WebElement(xpath='//*[@id="address"]')
    confirmation_password = WebElement(xpath='//*[@id="password-confirm"]')
    btn_register = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]')
    check_window = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div/div/h2')

    # EXP - 019
    login = WebElement(xpath='//*[@id="t-btn-tab-mail"]')
    btn_input_with_password = WebElement(xpath='//*[@id="standard_auth_btn"]')
    tab_login = WebElement(xpath='//*[@id="t-btn-tab-login"]')

    # EXP - 020
    tab_phone = WebElement(xpath='//*[@id="t-btn-tab-phone"]')

    # EXP - 021
    tab_mail = WebElement(xpath='//*[@id="t-btn-tab-mail"]')

    # EXP - 022
    tab_ls = WebElement(xpath='//*[@id="t-btn-tab-ls"]')

    # EXP - 026
    error_text = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')

    # EXP - 037
    email_imap = WebElement(xpath='//*[@id="address"]')
    f_code = WebElement(xpath='//*[@id="rt-code-0"]')
    btn_c = WebElement(xpath='//*[@id="otp_get_code"]')
