from behave import given, when, then
from selenium import webdriver
from pages.mercado_libre_bus import BuscarMercadoLibre

@given('el usuario se encuentra en la pagina base de mercado libre')
def step_give_intu_login(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.mercadolibre.com.co/')
    context.mercado_libre_bus = BuscarMercadoLibre(context.driver)
    


@when('el usuario busca el producto iphone13')

def step_when_intu_login(context):
    context.mercado_libre_bus.search('IPHONE 13')
    context.driver.implicitly_wait(10)

@then('aparecen todos los productos disponibles')

def step_then_intu_login(context):
    assert "iPhone" in  context.mercado_libre_bus.isElementPresent()
    