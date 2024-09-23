import allure
from selene import browser, have
from utils.methods import add_product_to_cart, clear_cart


def test_add_phone_cover_to_cart(auth_with_api):
    with allure.step('Вход на сайт авторизованным пользователем'):
        browser.open('/')
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': auth_with_api})
        browser.open('/')

    with allure.step('Проверка статуса добавления товара в корзину'):
        response_code = add_product_to_cart(product_url='/addproducttocart/details/80/1', cookie=auth_with_api, data={
            'product_attribute_80_2_37': 112,
            'product_attribute_80_1_38': 114
        })
        assert response_code == 200

    with allure.step('Переход в корзину'):
        browser.element('.ico-cart .cart-label').click()

    with allure.step('Отображение товара в корзине'):
        browser.element('.product-name').should(have.text('Phone Cover'))

    clear_cart()


def test_add_polkadot_top_to_cart(auth_with_api):
    with allure.step('Вход на сайт авторизованным пользователем'):
        browser.open('/')
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': auth_with_api})
        browser.open('/')

    with allure.step('Проверка статуса добавления товара в корзину'):
        response_code = add_product_to_cart(product_url='/addproducttocart/details/5/1', cookie=auth_with_api, data={
            'product_attribute_5_7_1': 3
        })
        assert response_code == 200

    with allure.step('Переход в корзину'):
        browser.element('.ico-cart .cart-label').click()

    with allure.step('Отображение товара в корзине'):
        browser.element('.product-name').should(have.text('Rockabilly Polka Dot Top'))

    clear_cart()
