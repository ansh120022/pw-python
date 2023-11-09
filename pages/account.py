class Account:
    def __init__(self, app):
        self.app = app
        self.balance_button = 'BUTTON[class="button money"]'

    def get_account_balance(self) -> float:
        self.app.reload()
        balance = self.app.locator(self.balance_button)
        value = balance.inner_text()
        numeric_value = float(value.split('€')[1])
        return numeric_value

    def top_up(self):
        self.app.locator(self.balance_button).click()
        self.app.locator('SELECT[class="form-input"]').select_option(value='FastTrackBonus + 500%')
        self.app.get_by_text('Card').click()
        self.app.get_by_text('€500').click()
        self.app.get_by_text('Deposit Approved').click()
        self.app.locator('DIV[class="modal__x"]').click()