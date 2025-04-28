from behave import given, when, then
from selenium import webdriver
from pages.wikipedia_search import BuscarWikipedia

@given('el usuario se encuentra en la pagina base de Wikipedia')
def step_give_intu_login(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://es.wikipedia.org/wiki/Wikipedia:Portada')
    context.wikipedia_search = BuscarWikipedia(context.driver)
    


@when('el usuario busca el lenguaje de programacion python')

def step_when_intu_login(context):
    context.wikipedia_search.search('Python')
    context.driver.implicitly_wait(10)

@then('aparece la informacion de python con su titulo')

def step_then_intu_login(context):
    assert "Python" in  context.wikipedia_search.isElementPresent()
    