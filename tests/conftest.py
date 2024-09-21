import pytest
import requests
from dotenv import load_dotenv
from selene import browser
import os
import allure
from allure_commons.types import AttachmentType


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(autouse=True)
def browser_management(request):
    with allure.step('Настройка браузера'):
        browser.config.base_url = os.getenv('URL')
        # browser.config.timeout = 6.0
        browser.config.window_height = 1080
        browser.config.window_width = 1920

    yield

    with allure.step('Закрытие браузера'):
        browser.quit()


@pytest.fixture()
def auth_with_api():
    with allure.step('Авторизация'):
        login = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')
        url = os.getenv('URL')
        response = requests.post(
            url=url + "/login",
            data={"Email": login, 'Password': password},
            allow_redirects=False
        )
        cookie = response.cookies.get('NOPCOMMERCE.AUTH')
        allure.attach(body=response.text, name='Response', attachment_type=AttachmentType.TEXT, extension='.txt')
        allure.attach(body=cookie, name='Cookie', attachment_type=AttachmentType.TEXT, extension='.txt')
        return cookie
