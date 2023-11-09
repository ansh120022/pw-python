from random import choice
from time import sleep


class Game:
    def __init__(self, app):
        self.app = app
        self.cats = ["/_nuxt/img/cat1.9386b22.png", "/_nuxt/img/cat2.248e071.png", "/_nuxt/img/cat3.585a357.png", "/_nuxt/img/cat4.fc0f54a.png"]

    def get_game_balance(self):
        sleep(1)
        balance = self.app.frame_locator('iframe').locator("//div[contains(text(),'Balance')]")
        value = balance.inner_text()
        numeric_value = float(value.split('€ ')[1])
        return numeric_value

    def open_game(self):
        self.app.locator("DIV[id='navigation']").click()
        self.app.locator("//a[.='Casino']").click()

    def get_bet_value(self):
        value = self.app.frame_locator('iframe').locator("//select/option[@selected='selected']").get_attribute("value")
        return float(value)

    def click_cat(self):
        random_cat = choice(self.cats)
        sleep(2)
        self.app.frame_locator('iframe').locator(f"//img[@src='{random_cat}']").click()
        win_amount = self.app.frame_locator('iframe').locator("//h1[contains(text(), 'Congratulations')]/following-sibling::h2/span").inner_html()
        if win_amount == '€0':
            return 'loss'
        else:
            return float(win_amount.split('€')[1])