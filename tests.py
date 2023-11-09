from in_python.pages.registration import Registration
from in_python.pages.account import Account
from in_python.pages.game import Game
from time import sleep


def test_registration(app):
    Registration(app).registration()


def test_deposit(app, login):
    account = Account(app)
    initial_value = account.get_account_balance()
    account.top_up()
    updated_value = account.get_account_balance()
    assert updated_value == initial_value + 500


def test_game(app, login):
    account = Account(app)
    initial_balance = account.get_account_balance()
    game = Game(app)
    game.open_game()
    result = game.click_cat()
    bet = game.get_bet_value()
    sleep(2)
    if result == 'loss':
        expected_result = initial_balance - bet
    else:
        expected_result = initial_balance + result - bet
    assert expected_result == game.get_game_balance()








