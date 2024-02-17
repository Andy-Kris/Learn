import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
driver = uc.Chrome(version_main=108)
driver.get('https://www.avito.ru/all/bytovaya_tehnika?q=%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE')


class AvitoParse:
    def __init__(self, url: str, items: list, count=100, version_main=None):
        self.url = url
        self.items = items
        self.count = count
        self.version_main = version_main

    def __set_up(self):
        self.driver = uc.Chrome(version_main=self.version.main)

    def __get_url(self):
        self.driver.get(self.url)

    def __paginator(self):
        while self.driver.find.elements(By.CSS_SELECTOR, "[data-marker='pagination-button/next']") and self.count > 0:
            self.__parse_page()
            self.driver.find.elements(
                By.CSS_SELECTOR, "[data-marker='pagination-button/next']").click()
            self.count -= 1

    def __pars_page(self):
        titles = self.driver.find_elements(
            By.CSS_SELECTOR, "[data-marker = 'item']")
        for title in titles:
            name = title.find_elements(
                By.CSS_SELECTOR, "[itemprop='name']").text
            description = title.find_elements(
                By.CSS_SELECTOR, "[class*='iva-item-description']").text
            url = title.find_elements(
                By.CSS_SELECTOR, "[data-marker='item-title']").getattribute("href")
            price = title.find_elements(
                By.CSS_SELECTOR, "[itemprop='price']").getattribute("content")
            print(name, description, url, price)

    def pars(self):
        self.__set_up()
        self.__get_url()
        self.__paginator()


if __name__ == "__main__":
    AvitoParse(url='https://www.avito.ru/all/bytovaya_tehnika?q=%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE',
               count=1,
               version_main=108,
               items=["iphone"]
               ).parse()
