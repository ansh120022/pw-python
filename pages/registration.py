from time import sleep


class Registration:
    def __init__(self, app):
        self.app = app

    def submit_form(self):
        self.app.locator('BUTTON[type="submit"]').click()

    def login(self):
        self.app.goto("https://demo.ft-crm.com/")
        self.app.get_by_text('Returning user').click()
        self.app.locator('INPUT[type="email"]').fill('ansh00000@gmail.com')
        self.submit_form()
        sleep(1) # let the browser save cookie

    def registration(self):
        self.app.goto("https://demo.ft-crm.com/")
        self.app.get_by_text('New user').click()
        self.app.get_by_text('I GET IT, CONTINUE').click()
        self.app.locator('.input').fill('ansh00000@gmail.com')
        self.submit_form()
        self.app.locator('INPUT[type="text"]').fill('+357')
        self.app.locator('INPUT[type="number"]').fill('9690000')
        self.submit_form()
        self.app.locator('INPUT[type="text"]').fill('Anastasiia Sh')
        self.submit_form()
        self.app.locator('INPUT[type="password"]').fill('MYsPASS_999!')
        self.submit_form()

