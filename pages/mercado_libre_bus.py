from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class BuscarMercadoLibre(BasePage):
    SEARCH_TEXT = (By.ID, 'cb1-edit')
    TEXTIPHONE = (By.CLASS_NAME, 'poly-component__title')
    SEARCH_BUTTON = (By.XPATH, '/html/body/header/div/div[2]/form/button')
    

    def search(self,search_text):
        self.enter_text(self.SEARCH_TEXT, search_text)
        self.click(self.SEARCH_BUTTON)
        

    def isElementPresent(self):
        elemento = self.find_element(self.TEXTIPHONE)
        texto = elemento.text
        return texto