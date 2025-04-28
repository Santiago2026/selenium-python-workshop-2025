from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class BuscarWikipedia(BasePage):
    SEARCH_TEXT = (By.XPATH, '/html/body/div[1]/header/div[2]/div/div/div/form/div/div/div[1]/input')
    TEXTPYTHON = (By.XPATH, '/html/body/div[2]/div/div[3]/main/header/h1/span')
    SEARCH_BUTTON = (By.XPATH, '/html/body/div[1]/header/div[2]/div/div/div/form/div/button')
    BUTTON_SEARCH1= (By.XPATH, '/html/body/div[1]/header/div[2]/div/a/span[1]')
    

    def search(self,search_text):
        self.click(self.BUTTON_SEARCH1)
        self.enter_text(self.SEARCH_TEXT, search_text)
        self.click(self.SEARCH_BUTTON)
        

    def isElementPresent(self):
        elemento = self.find_element(self.TEXTPYTHON)
        texto = elemento.text
        return texto